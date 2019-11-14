# A Code injection Method for Rapid Docker Image Building

**abstract:** xdd

**index-terms:** xdd

## Introduction

In the very early days of software development. The developers build a run an application, host it on host machine and run. As the usage of the application increases, the user would have to find machines with higher capacity. Even on a single machine, software dependencies of application the first instance makes it hard to adjust a different set of dependencies for another application cohosted on the same machine. To address the rididity of resource and lack of isolation, developers gradually switch to container infrastrcutre. At first developers uses Linux Container (LXC) which uses Linux namespace, a kernel feature that partition a set of resource for a set of processes exclusively, and control group (cgroup), a kernerl feature that limits and isolate machine resource usage. While LXC is useful in system level containerization, Docker developed containers for applications based on the same principle. Developers write the code, specifies imperiative procedures in a dockerfile, then use the Dockerfile to build an Image. An image wraps all the necessary dependencies in a bundles. The user can deploy the image anywhere in a container. A container is a running instance that is isolated from any other environment. Extending on the container infrastructure, people are able to set up microservice architecture, and build continous integration pipeline in which Docker spawn up a new container in which it perform all tests, so the application's code does not break the pipeline's host machine.

### Image Layers

When building Docker images, Docker writes each run statement as an image layer. Layers are sorted in structural order from the base up. When docker traverse down the Dockerfile, statement creates a new layer. Each new layer encompasses all files created during such a runtime. Each Layer generated will be assigned a corresponding and permanent ID. Even if the developer change the content of the layer entirely, the layer still has the same ID. Figure 1 shows the Docker's step by step building of an image from a Dockerfile. Notice after each build, docker informs the user of each layer's ID. To examine what command each layer correspond to the user can run 'docker history image:tag'. By default, all layers are stored in '/var/lib/docker/aufs/diff'. The developer can even export the image by 'docker save image:tag > file.tar' and load it by 'docker load < file.tar'. The layering architecture and easiness to transport images make Docker construction very flexible. When the image is already constructed once on local machine, by default each layer is cached. If the developer choose to update a line of code that concern only one layer, that layer is reconstructed and the rest uses the cached version.

### Docker Layer Caching (DLC) Mechanism

After inital docker image construction, Docker saves cache as intermediate images hidden from 'docker images' list. When the developer runs build image again, docker looks at the following field to determine wether or not to use the cache:

1. Use the parent image as the starting point, pull out its manifest and examine checksums and UUID of its child images to see if the new build is identical as the existing image. If true, skip build.

2. Examine new version of Dockerfile to see if instruction has been added, remove or altered, if true, remove or alter the corresponding layer.

3. For 'ADD', 'COPY' that are altered, compute checksum of updated files, compare it against existing files if the checksum does not match, 'copy', or 'ADD' new files to build. The checksum uses sha256 hash algorithm and last modified and last accessed time are not taken into consideration. If they match, use cache.

4. For operation commands including but not limited to 'RUN', 'CMD', 'ENTRYPOINT', Docker checks the literal message without checking the corresponding files. for example, for command 'RUN apt install ubuntu' the literal command is checked instead of comparing every single files of ubuntu in the new version against the old version.

### Deduplication

In data science, the term deduplication refers to removing copies of data that are repetitive leaving one copy of data in existence. Docker also uses this principle when constructing images. Say a new version of an image only has one new layer, docker tags the UUID of already built layers from registry and only build the new layer that is needed. In Docker hub only 10% of layers are used by more than 2 images, and only 1% used by more than 3 images. In the grand scale of things deduplication is not as common amongst all images. Yet, on a development perspective, deduplication is quite common as developers rapidly updates their application and build image for testing.

### Problem and Proposal

As the application grows, a Dockerfile grows in complexity and volumes, so do code and tests. Coupled with the complex deployment scenarios, building images in large application becomes extremely time consumming. Sometimes updating a single layer would take more than 10 minutes in a 20GiB application given complex build requirements: conda, make etc. Modern software development process encourages a build after each small incremental change such that a pipeline checks for wether the new feature update works as intended. This becomes problematic when we have a high demand of builds but a low thorougput of build runtime which is  clogged up by long build time. Utilizing the cache feature after each build and layers stored after dedpulication, we propose a methodology that injects newly edited code into existing docker image layer while bypassing the sha256 checksum rule to enale rapid docker image building withing actually building. This reduces o(n) linear runtime required for updating an image where n = size of the layer to a constant O(1) runtime for limited numebr of scenarios.

## Process

### code injection

Talk about the update methodology in detail here

### Checksum bypass

How we byass the checksum

### redeployment

How the new image is not confused with the old image, the 2 stands side by side.

## Performance and Benchmarking

### Setup format

This could be a docker plugin, but for the sake of this report demonstration (aim to finish this in one week, let's do a script. External script would definitely drag down the speed, let's just optimize it to be faster than the current solution )

### Result

- comapre python one line application 100 trials inject 1 line
- compare java one line application 100 tirals inject 1 line
- compare complex python app 100 trials inject 5(,or 50 or 500) lines
- compare complex java app 100 trials inject 5-50 (or even500) lines

## limitations

Beacause this uses literal injection, integrity cannot be guaranteed for compiled programming languages as compiling to binary code may behave differently than their original program code. Minor discrepencies can possibily lead to great disaster.

Multi layer injection is possible but not within the scope of this paper. The concept would be performing similar.

## Conclusion and Recomandation


# Reference
https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612

