For the project to work, install Docker on your local machine and then execute mentioned commands from terminal

## Docker Installation
## Ubuntu
Link -> https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

## Mac OS
Link -> https://docs.docker.com/docker-for-mac/install/#where-to-go-next

## Windows 10
Link -> https://docs.docker.com/docker-for-windows/install/#download-docker-for-windows  
Open and Run the file.  
Follow instructions. You might have to sign out and Restart your windows for docker to start

### Enable Hyper -V on your machine  
Run powershell as admin and enter the below command  
Enable-WindowsOptionalFeature -Online -FeatureName:Microsoft-Hyper-V -All  
Link -> https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v

### Enable Virtualisation in BIOS  
Reboot your windows and go to BIOS  
Enable Virtualisation   
Link -> http://www.sysprobs.com/disable-enable-virtualization-technology-bios

# Instructions to run the project
### Open Powershell/Terminal as admin/root user   
(For windows, ignore "sudo" keyword)
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
