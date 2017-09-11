import pika
import requests
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello',body=message)
    # print( " [x] Sent 'Hello World!' ")
    connection.close()
    return "Message Sent!  "

@app.route("/greeting", methods=['GET', 'POST'])
def say_hello():
	message = str(request.args.get('text'))
	print("Message : "+message)
	# message = "Hello RabbitMQ from Python"
        ack = send_to_queue(message)
	return ack + "------------->" + message

@app.route("/call_java_node")
def call_java_node():
	r = requests.get("http://localhost:8080/hi")
	s = requests.get("http://localhost:3000/api/sayhello")
	return  "Response recieved from Java :: Response recieved from Node"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

