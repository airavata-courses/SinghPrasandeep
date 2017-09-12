import pika
import requests
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

received_msg = ""

def send_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='', routing_key='hello',body=message)
    # print( " [x] Sent 'Hello World!' ")
    connection.close()
    return "Message Sent!  "

def callback(ch, method, properties, body):
    print(" [x] Recieved %r" % body)
    # ch.stop_consuming()
    # global received_msg
    # received_msg = body
    # ch.stop_consuming()

@app.route("/receive")
def receive_from_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel  =  connection.channel()
    channel.queue_declare(queue='hello')
    method_frame, header_frame, body = channel.basic_get(queue = 'hello')
    if method_frame.NAME == 'Basic.GetEmpty':
        connection.close()
        return ''
    else:
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        connection.close()
        print("Received message :"+body)
        return "Received message ------------> "+body
 
@app.route("/greeting", methods=['GET', 'POST'])
def say_hello():
	message = str(request.args.get('text'))
	print("Sent Message : "+message)
	ack = send_to_queue(message)
	return ack + "-------------> " + message

@app.route("/call_java_node")
def call_java_node():
	r = requests.get("http://localhost:8080/hi")
	s = requests.get("http://localhost:3000/api/sayhello")
	return  "Response recieved from Java :: Response recieved from Node"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

