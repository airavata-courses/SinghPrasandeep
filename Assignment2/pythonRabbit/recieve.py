import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel  =  connection.channel()

# This declaration acts as a safety check, if this code is run before the send program : this will create a new queue
# Else it will use the queue specified in the command below
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
	print(" [x] Recieved %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [x] Waiting for messages. To exit press  CTRL+C')
channel.start_consuming()

