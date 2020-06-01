#!/usr/bin/env python
import pika
import sys
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='s5', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_key = 'KRATOS'

channel.queue_bind(exchange='s5', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def relsim(payload):
    print(" [RELSIM] %r" % (payload))

def relput(payload):
    print(" [RELPUT] %r" % (payload))

def relstart(payload):
    print(" [RELSTART] %r" % (payload))

switcher = {
    'RELSIM': relsim,
    'RELPUT': relput,
    'RELSTART': relstart
}

def callback(ch, method, properties, body):
    message = json.loads(body)
    func = switcher.get(message['type'], "nothing")
    func(message['payload'])  

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()