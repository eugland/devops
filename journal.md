# Journal of Work at Huawei

```json
me: {
    Company: Huawei
    Job: Assistant Engineer
    Role: Devops, Infrastructure Engineer
    Team: Infrastructure -> Platforms
    Department: Noah's Ark -> 2012 Labratory 
    Location: Markham
}
```

## August 19

- use docker version 19.3.1, see if we can remove dependencies to nvidia docker
- Also nvidia docker deprecates in this version

    ```bash
        docker run _it 
    ```

- look into gitlab fopr test, yoda_sw_display, health of system
- coverage test for yoda

## August 20

- obtained access fip and internet

## August 21 

- Continued internet setup waiting for Proxy

## August 22

- full proxy access, and control of machine

## August 23

### Cyber Secucirty: 

- Is avaliability, integrity, anti-attack, confidentiality, traceability
- prevents economic losses, reputation damages, civil, admin, find target of trade protectionism
- personal data -> data subject
- data controller
- data processor

### 七大准则

1. lawful transparent processing
2. purpose limitation
3. Data minimization
4. Accuracy
5. Retention period minimzation
6. Integrity and Confidentiality
7. Accountability

### BCG 原则

| Cyber Security | privacy |
|----|---|
|无授权|贩卖个人信息|
|入毒|乱用 |
|攻击|
|用第三方|

eu, singapore no cross border transfer of data

### Privacy Protection Training

1. make sure follow laws
2. avoid risk
3. avoid data leak
4. maximize all parties trust

### privacy - fundamental rights and friday

in digital society: - enhance following

- awareness
- policies
- processes
- supporting systems

=> EU, US, Singapore and region:

US: Federral

Eu: lateral Coverage

### why do we need to protect privacy

- The right to be left alone
- Viol: physical, Info privacy (Huawei General Privacy )
- personal data
  - sensitive: fund rights and freddom, life, genetic, health, identity, property, other
  - Business Contact personal: business communication- name position title mail

### General GDPR

- Unify data protection
- binding force, apply to EEA, EU
- ICO in UK 400k vs 59M

role | character | example
--- | --- | ---
data subject | can indentify | user of product
controller | determine purpose | Vmall
processor | process | Huawei Carrier

### Information Security in Huawei

- company has large assets and tangible either wa.
- protecting // especially technoligy and business
- Employees are responsible for protecting the contents
- **ISO/IEC 27001 is** is the most sttrivbuted used information security management standard in the world.

### work
- configure ROS Pycharm, python, Anaconda
- cloned needed repos
- remaining security notes no copied, and markdwon, and spesh 

## August 26 Monday
- Performed a reading on naturalistic driving

1. gynab behavioral social interation, conflict resolution
2. variability: driving styles, experience, etc
3. complexity, edge cases: perception
4. control problem: human in the loop mechanical system
5. The expected/ unexpected limitation, inperfections
6. reliance on the software: bugs, vunlnerabilities
7. Recognize when t otake control, adpt when needed
8. environment conditions
9. societal / individual tolerances to human-machine

HCAI, MIT-AVT 'naturalistic driving'
NDS naturalistic driving study

- driver uses their own vehicle
- drive in the wild

guiding principle: 

- autonomy at all levels: EBS autopilot
- beyond epochs and manual autonomation: crash and near crash vast remainder
- multiple study Duration. 
- observe in owned vehicles vs given
- multiple analysis modalities: CV, GPS, IMU, CAN  go to http :://hcai.mit.edu/avt
- MIT-AVT: gather naturlaistic driving data, build on the work and lessons learned of the earlier gen of NDs
- (SHRPZ): 2nd strategic highway research program
- Purpose: anotate Specific epochs of driving
- requiures large temporal window than an epoch of a few seconds, or even minutes. Large scale long tail of naturalistic driving data analysis is required
- We use DL for Driver state defction, driver body poses estimation, and vehicle state detection
- Dataset for application of Deep learning

## August 27- 30 
- Yet Unable to move to newer docker version because likely changes ti tge docker, the support for GPU is likely to be moved out into separate plugins
- CI/CD pipeline: jobs = basic configuration component, stages = stages keyword then build and deploy
- Regular package vs namespace package which allows for split of sub pakcages and modules within a single package
```bash 
$ make build    
```

## Semptember 9 - 10 Monday - Tuesday
- worked on the 2 pipe solution

## Semptember 11 Wednesday

### Work plan with Michael and Danson\

1. Migration 
  - nexus, reduce nexus for Arash
  - eval - nexus, perception - nexus
  - script sync old to new registry (on server)
  - remind infrastructure - kybe-base \[kyber-server\]
  - produce required scripts for server setup
  - run script, 
  - switch the flip gitlab.new redirect around to new one changes settings variables
2. Kyber-evaluation
- put artifacts into new gitlab registry

3. Kubernetes # poke Arash
- use case: 3 workers, 2 deploys cars ziggy, and car stardusts
- play rosbag - run entire stack - empty fault detection
- **ground truth** Image labelling as ground truth
- Is the msg sending contain anything? 
- msg suppose there, not htere?
- msg sent does not exist. 
- see topic on gitlab
- compile a script for kubernetes installation

4. Pipeline for perception team? dynodance? data pipe? spark? 

- context: obj detect -> stages -> model 
- train neural net based on ground truth, test against model, sometimes overfit occur, test set (blind test)


## September 12 Thursday
- perform coverage test
    ```bash
    yoda/data/data_source
    yoda/gui/
    yoda/registry/
    yoda/utils
    ```
-


## September 13 Friday
- Common in China: kybersim bridge, hmi tools, PNC planning and control 
- Canada: perception_l5, 
- both: pnc, fusion, modules

hence we need to
Diagram:
```
Yello:            /-> runnerB -\                 /-> runnerB --> Chinese registry
Ezone    common ==               ==> evaluation =               
Green:            \-> runnerA -/                 \-> runnerA --> Canadian registry
```
### Kubernetes 

- compute-d kubernetes master
- uses calicode with kudeam, apply (CNI) Container Network Interface
- problem: 
  - works 1st day, 2nd day down
- proxy -> go to internet -> interanet
- ip- range: printf -v pod '%s' 10.218.165.51
- preference
- destroy node -> run again -> desvelop tools to spin up 



## September 16 Monday
### stand up (YODA)
- yoda continuous and interval recording? 30s or 20 seconds? 
- processing between deletopns either
  - queueb ags record, next delete
  - low with storage then record delete, record again
- select topic -> add 2 checkboxes, sub selections how many rosbag you want to select
- kevin: propose keep dashcam recording as it goes, but yoda record when prompted
- separat scripts to add on, which is easy to commmence
- issue is mkz_driver still blocking

### standup Evaluation
- version of kypersim to sync with China
- Before go into ros bag, traffic light issue is need to be solved
- omniboard can waity
- run parallel EXperiment
- **Kyber-system ARASH has, I get it from him to gain Maintainer anywhere**

### knowledge Transfer from Michael
- Conda Recipies: construct, private construct, conda, conda.build
- Environment.yml 
  - Used in base image
  - Used on conda
  - makle file
  - make dev env | make build
  - conda recipe create .sh script binary
- make dist build base image, build repo
- meta.yml 
- add new library environmentally
- conda recepie, metal.yml <- installer

### registry

- green: 2 master, feature
- yellow:  1 in China
- pipeline builds images, by this logic, each stage should rely on base image
- How to configure permission and stuff
- renew jetty certificate
- MongoDB: readonly, (1) edit manually, (2) go iunto code to root user push changes

### Evaluation basic commands
```bash 
$ alias kcl='python -m kyber.evaluation'
$ kcl experiments run --viz --agent # 2 ids agent and scenario
$ kcl evaluator run --exp-id=<eventid>
```

