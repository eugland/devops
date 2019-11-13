# GKE Lesson
### Reference
* [Course-1-GCP](#course-1-gcp)
    * [gcp-cloud-arch-regions-pricing-api](#gcp-cloud-arch-regions-pricing-api)
    * [security](#security)
    * [reshierachy](#reshierachy)
    
    
## Course-1-GCP
### GCP-Cloud-Arch-Regions-Pricing-Api
GCP offers four main kinds of services: compute, storage, big data and machine learning. Cloud computing is on-demand self-service, over net anywhere, big-pool, elastic, pay per us. Cloud computing remove local infra set up, so Google got into container network. IaaS=IaaS offerings provide raw compute, storage, and network; PaaS=bind your code to library; SaaS=direct service over internet. GCP zone=a deployment area, region=independent geographical area round trip latency< 5ms. store more app in multi-zone in one region to fault tolerant. Run app in multi regions for better edge loading for customer all over the world. Charge by per seconds, auto safe on incremental minut when user more than 25% of an instance per month. Can specify how many CPU/memory. GCP has open source interface: Bigtable->Apache Hbase, Dataproc->Hadoop
, ML->tensorflow, k8s->any code, stackdriver->monitor workloads. 

### Security
Titan chip for machines, cryptographic signature to maksure the booting is correct. Multiple physical security protections, crptoprivacy and integrity for remote procedure data-on-the-network Infra encrypts data, intelligently challenge given rise on risk factor. U2F devices to login. 

### reshierachy
project->folders(nestable)-> organization. Policy on indi resources too, and inherited downwards. Project for enabling, using GCP services, apis, billing, members. project res one to one; project owner, users many to many. id(edit, perm), name(edit), number(assigned). Folder-> admin rights-> have an org. from strict to lax top to bottom.

### IAM
who->(user, service account), what->(action premission: primitive->owner,editor,viewer; predefined, custom), which->resource. Roles: list,read, chang, start/stop. least priviledged model. custome cannt folder. Give compute engine priviledge not people -> service account which is also a resource. Create different svcAcc for part of app. need to edit and part that needs viwe only.

### VPC-CE-Storage
segmetn network using firewall rules to restrict access to instacnes, create static rouets to forward traffic. global scope, can have subnet can span region. Has iptables can route internally; cna define firewall rules; can peer other VPC; can balance traffic http, https, tcp, udp and ssl. Compute engine are virtual machine spawn from snapshot images. preemptibl  can stop and save money. 
Cloud storage: object blob stored in buckets. ACL: access control list. tiers are regional, multiregional, nearline, coldline. 
Cloud BigTable: NoSQL scalable, low latency, high thruput correspond to HBase
Cloud SQL： mySQL + postgres SQL 
Cloud Spanner: SQL horizontal scalable transactional consistency
Datastore: noSQL but transactional and SQL like querie, good for games. 

### App-Engine
PaaS: Deploy coed directly with library binding. Built in service: memory-caching, load balacin , haelth, log, authetnicate, etc. autoscale. STD env: low util app = no charge. std provision specific runtime: java, python etc. Can't write to local must write to persistent 60s timeout, no third party binary, Also there is Flexible env. Exposes api with Cloud Endpoint for dev an apigee for prod. IaC, Cloud repo, Deploy manager, edit deploy template that specify how app engine will look like. 

### BIG Data platform
You can monitor stackdriver with 
