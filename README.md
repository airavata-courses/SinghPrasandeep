

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
sudo docker pull singhprasandeep/java-node-python

### To Run node and express microservice : Use :  
sudo docker run -d -w /node-service -p 3000:3000 singhprasandeep/java-node-python npm start  
Go to localhost:3000/api/sayhello to check

### To Run python microservice : Use :  
sudo docker run -d -w /service-python -p 5000:5000 singhprasandeep/java-node-python python api.py
Go to localhost:5000/greeting to check

### To Run java microservice : Use :  
sudo docker run -d -w /java-service -p 8080:8080 singhprasandeep/java-node-python java -jar target/gs-spring-boot-docker-0.1.0.jar 
Go to localhost:8080/hi to check

### To Run server for hosting user interface  
sudo docker run -d -w /server-ui -p 8000:8000 singhprasandeep/java-node-python python server_ui.py
Go to localhost:8000 to check

Open browser and hit **localhost:8000** to start the application
You will be presented with 3 buttons each representing a microservice  
Click on the buttons to get response from the respective microservice
