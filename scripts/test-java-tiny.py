import os
import sys
import argparse
import subprocess
import re
import time
import shutil
import tarfile
import json
import glob
import hashlib
import csv

def build_image(image_name):
    p = subprocess.Popen("sudo docker build -t {} .".format(image_name), stdout=subprocess.PIPE, shell=True)
    p.wait()


def modify_image():
    with open("appl/build/libs/nasapicture-0.0.1-SNAPSHOT.war", "a") as f:
        # simulate we have compiled the new source code --- war is updated
        for i in range(0, 1):
            f.write("print('hello_world')\n")

def get_build_time(image_name, changed_step):

    my_env = os.environ.copy()
    my_env["PYTHONUNBUFFERED"] = "1"

    pattern = re.compile("Step *\/*")
    start_time = 0
    p = subprocess.Popen("sudo docker build -t {} .".format(image_name), stdout=subprocess.PIPE, bufsize=1, env=my_env, shell=True)

    while p.poll() is None:
        line = p.stdout.readline().decode('utf-8')
        if not line: 
            break

        if pattern.match(line):
            if line.split("/")[0][-1] == str(changed_step):
                start_time = time.time()

    return time.time()-start_time


def save_image(image_name, save_dir):
    os.mkdir(save_dir)
    save_name = image_name.replace(":", "_") + ".tar"
    p = subprocess.Popen("sudo docker save {} > temp/{}".format(image_name, save_name), stdout=subprocess.PIPE, shell=True)
    p.wait()

    return save_name


def decompose_image(image_tar_path):
    with tarfile.open(image_tar_path) as tar:
        tar.extractall("temp")

def sync_files(srcdir, destdir):
    shutil.copyfile(os.path.join(srcdir, "appl/build/libs/nasapicture-0.0.1-SNAPSHOT.war"),os.path.join(destdir, "usr/app/app.war")) 

def inject_code(image_tar_path, changed_step):
    json_files = glob.glob("temp/*.json")
    manifest_json_f = os.path.join(os.path.dirname(image_tar_path), "manifest.json")
    config_json_f = [f for f in json_files if f != manifest_json_f][0]
    changed_layer_hash = 0

    # find the changed layer hash
    with open("Dockerfile") as f:
        step_count = 0
        non_empty_layer_step_cnt_after_changed_step = 0
        for line in f.readlines():
            if line.strip():
                step_count += 1
                if (step_count > changed_step) and ("COPY" in line.upper() or "ADD" in line.upper()):
                    non_empty_layer_step_cnt_after_changed_step += 1

    with open(manifest_json_f) as f:
        manifest_json = json.load(f)
        layers = manifest_json[0]["Layers"]
        changed_layer_hash = layers[len(layers)-non_empty_layer_step_cnt_after_changed_step-1].split("/")[0]
    
    changed_layer_dir = os.path.join("temp", changed_layer_hash)
    changed_layer_tar = os.path.join(changed_layer_dir, "layer.tar")

    # extract the files in that layer and update the files (code injection)
    with tarfile.open(changed_layer_tar) as tar:
        tar.extractall(changed_layer_dir)

    sync_files("./", changed_layer_dir)

    os.remove(changed_layer_tar)
    with tarfile.open(changed_layer_tar, "w") as tar: 
        for f in os.listdir(changed_layer_dir):
            if f not in ["json", "VERSION", "layer.tar"]:
                tar.add(os.path.join(changed_layer_dir, f), arcname=f)
                if os.path.isdir(os.path.join(changed_layer_dir, f)):
                    shutil.rmtree(os.path.join(changed_layer_dir, f))
                else:
                    os.remove(os.path.join(changed_layer_dir, f))

    # update the diff id of the changed layer in config json file
    changed_layer_diff_id = hashlib.sha256(open(changed_layer_tar).read()).hexdigest()

    with open(config_json_f, "r+") as f:
        config_json = json.load(f)
        diff_ids = config_json["rootfs"]["diff_ids"]
        diff_ids[len(diff_ids)-non_empty_layer_step_cnt_after_changed_step-1] = "sha256:{}".format(changed_layer_diff_id)
        config_json["rootfs"]["diff_ids"] = diff_ids

        f.seek(0)
        json.dump(config_json, f)
        f.truncate()

    # os.remove(image_tar_path)
    # with tarfile.open(image_tar_path, "w") as tar: 
    #     for f in os.listdir("temp"):
    #         if f != os.path.basename(image_tar_path):
    #             tar.add(os.path.join("temp", f), arcname=f)

    # load the image
    # p = subprocess.Popen("sudo docker load < {}".format(image_tar_path), stdout=subprocess.PIPE, shell=True)
    # p.wait()

def get_code_injection_time(image_tar_path, changed_step):
    start_time = time.time()
    inject_code(image_tar_path, changed_step)
    return time.time() - start_time

def clean_up(image_name):
    shutil.rmtree("temp")

    p = subprocess.Popen("sudo docker images", shell=True, stdout=subprocess.PIPE)
    outs, errs = p.communicate()
    image = image_name.split(":")[0]
    tag = image_name.split(":")[1]
    for line in outs.decode('utf-8').splitlines():
        if (image in line and tag in line) or "<none>" in line:
            image_hash = line[43:55]

            p2 = subprocess.Popen("sudo docker rmi {}".format(image_hash), stdout=subprocess.PIPE, shell=True)
            p2.wait()

rebuilt_time = []
inject_time = []

def test_one(args):
    build_image(args.image)

    saved_as = save_image(args.image, "temp") # this is the origional build

    modify_image()
    t = get_build_time(args.image, args.changed_step)
    rebuilt_time.append(t)
    with open("results1.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([t])
    
    decompose_image(os.path.join("temp", saved_as))
    saved_as = "hello_latest"

    t = get_code_injection_time(os.path.join("temp", saved_as), args.changed_step)
    inject_time.append(t)
    with open("results2.csv", "a") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow([t])

    clean_up(args.image)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", action="store", type=str)
    parser.add_argument("changed_step", action="store", type=int)

    args = parser.parse_args()

    for i in range(0, 100):
    	print(i)
        test_one(args)

    with open("results.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        for i, v in enumerate(rebuilt_time):
            writer.writerow([v, inject_time[i]])

if __name__ == "__main__":
    main()
