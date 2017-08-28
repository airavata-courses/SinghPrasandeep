## Instructions - Ubuntu

### Install Docker 
Link -> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04


### Pull Docker Image from DockerHub  
sudo docker pull singhprasandeep/node-python-java

### To Run node and express microservice : Use :  
sudo docker run -d -w /microservice -p 9000:3000 singhprasandeep/node-python-java npm start  
Go to localhost:9000/api/sayhello to check

### To Run python microservice : Use :  
sudo docker run -d -w /python-microservice -p 5000:5000 singhprasandeep/node-python-java connexion run my_api.yaml -v  
Go to localhost:5000/greeting to check

### To Run java microservice : Use :  
sudo docker run -d -w /java-microservice -p 8080:8080 singhprasandeep/node-python-java java -jar target/gs-spring-boot-docker-0.1.0.jar  
Go to localhost:8080/hi to check


