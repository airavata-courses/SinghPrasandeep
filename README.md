## Instructions 
### Must have Docker installed and started. 
Link -> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04


# 1 - java-microservice
Pull the microservice from DockerHub  
docker pull singhprasandeep/java-microservice:firsttry

Run using the command  
docker run --rm -p 8080:8080 singhprasandeep/java-microservice:firsttry  
Go to localhost:8080 to check

# 2 - To Run 2 microservices
Pull the microservice from DockerHub  
sudo docker pull singhprasandeep/ubuntu-node-python

To Run node and express microservice : Use :  
sudo docker run -d -w /microservice -p 9000:3000 singhprasandeep/ubuntu-node-python npm start
Go to localhost:9000/api/sayhello to check

To Run python microservice : Use :  
sudo docker run -d -w /python-microservice -p 5000:5000 singhprasandeep/ubuntu-node-python connexion run my_api.yaml -v
Go to localhost:5000/greeting to check



