#!/bin/bash
time gradle build -p app/
time docker build -t java-tiny-decompose:latest .

if [ $1 ] && [ $1 = "run" ] 
then  
    if [ $2 ] && [ $2 = "-d" ] 
    then 
        docker run -d -p8080:80  java-tiny-decompose:latest 
    elif [ $2 ] && [ $2 = "-it" ] 
    then 
        docker run -p8080:80 -it java-tiny-decompose:latest sh
    else
        docker run java-tiny-decompose:latest
    fi 
    
fi 