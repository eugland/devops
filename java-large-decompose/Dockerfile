# Mother fucker here
# http://sparkjava.com/tutorials/docker
# bad java dockerfile https://codefresh.io/docker-tutorial/java_docker_pipeline/

FROM ubuntu:latest
RUN apt update
RUN apt install -y openjdk-8-jdk  maven 

WORKDIR /code

# Prepare by downloading dependencies
ADD pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
ADD src /code/src
RUN ["mvn", "package"]

EXPOSE 4567
CMD ["/usr/lib/jvm/java-8-openjdk-amd64/bin/java", "-jar", "target/sparkexample-jar-with-dependencies.jar"]Copy
