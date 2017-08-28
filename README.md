## Instructions to run individual microservices on local machine
### Must have Docker installed and started. Link -> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

### All dependencies are already installed in the docker image

# 1 - java-microservice
Pull the microservice from DockerHub  
docker pull singhprasandeep/java-microservice:firsttry

Run using the command  
docker run --rm -p 8080:8080 singhprasandeep/java-microservice:firsttry  
Go to localhost:8080 to check

# 2 - node-microservice
Pull the microservice from DockerHub  
docker pull singhprasandeep/node-microservice 

Run using the command  
sudo docker run -d -w /microservice -p 9000:3000 singhprasandeep/node-microservice npm start  

Go to localhost:9000/api/sayhello to check


