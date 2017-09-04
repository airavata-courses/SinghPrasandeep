import requests
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/greeting")
def say_hello():
	return "Hello Docker from Python!";

@app.route("/call_java_node")
def call_java_node():
	r = requests.get("http://localhost:8080/hi")
	s = requests.get("http://localhost:3000/api/sayhello")
	return  "Response recieved from Java :: Response recieved from Node"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
