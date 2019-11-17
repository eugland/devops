#FROM ubuntu:18.04
FROM continuumio/miniconda3
COPY . /root/
WORKDIR /root
RUN apt update && apt install curl git less gedit -y 
#RUN sh miniconda.sh -b
#ENV PATH="/root/miniconda3/bin:$PATH"
#RUN conda install -y constructor
# RUN conda install constructor
# RUN constructor .
RUN conda env update -f environment.yaml
CMD ["python", "main.py"]

