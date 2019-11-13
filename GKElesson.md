# GKE Lesson
### Reference
1. [Course-1-GCP](#course-1-gcp)
  a. [gcp-cloud-arch-regions-pricing-api](#gcp-cloud-arch-regions-pricing-ap)

## Course-1-GCP
### GCP-Cloud-Arch-Regions-Pricing-Api
GCP offers four main kinds of services: compute, storage, big data and machine learning. Cloud computing is on-demand self-service, over net anywhere, big-pool, elastic, pay per us. Cloud computing remove local infra set up, so Google got into container network. IaaS=IaaS offerings provide raw compute, storage, and network; PaaS=bind your code to library; SaaS=direct service over internet. GCP zone=a deployment area, region=independent geographical area round trip latency< 5ms. store more app in multi-zone in one region to fault tolerant. Run app in multi regions for better edge loading for customer all over the world. Charge by per seconds, auto safe on incremental minut when user more than 25% of an instance per month. Can specify how many CPU/memory. GCP has open source interface: Bigtable->Apache Hbase, Dataproc->Hadoop
, ML->tensorflow, k8s->any code, stackdriver->monitor workloads. 

## Security
Titan chip for machines, cryptographic signature to maksure the booting is correct. Multiple physical security protections, crptoprivacy and integrity for remote procedure data-on-the-network Infra encrypts data, intelligently challenge given rise on risk factor. U2F devices to login. 

## reshierachy
project->folders(nestable)-> organization. Policy on indi resources too, and inherited downwards. Project for enabling, using GCP services, apis, billing, members. project res one to one; project owner, users many to many. id(edit, perm), name(edit), number(assigned). Folder-> admin rights-> have an org. from strict to lax top to bottom.
