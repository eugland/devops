FROM java:8-jdk-alpine
COPY ./appl/build/libs/nasapicture-0.0.1-SNAPSHOT.war /usr/app/app.war
EXPOSE 8080
CMD ["/usr/bin/java", "-jar", "-Dspring.profiles.active=default", "/usr/app/app.war"]
