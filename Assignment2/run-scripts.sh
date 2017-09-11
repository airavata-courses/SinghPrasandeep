sudo docker pull singhprasandeep/node-python-java
echo "------------------Image pulled------------------"
sudo docker run -d -w /service-python -p 5000:5000 singhprasandeep/java-node-python python api.py
echo "------------------python server up!-------------"
sudo docker run -d -w /java-service -p 8080:8080 singhprasandeep/java-node-python java -jar target/gs-spring-boot-docker-0.1.0.jar
echo "------------------java server up!---------------"
sudo docker run -d -w /node-service -p 3000:3000 singhprasandeep/java-node-python npm start
echo "------------------node server up!---------------"
sudo docker run -d -w /server-ui -p 8000:8000 singhprasandeep/java-node-python python server_ui.py
echo "------------------UI server up!-----------------"
