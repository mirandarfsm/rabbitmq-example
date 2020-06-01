#!/usr/bin/env python
import pika
import sys
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='s5', exchange_type='topic')

routing_key = 'KRATOS'
data = { 'type': 'RELSTART', 'payload': { 'name': 'abc', 'year': 10 } }

message = json.dumps(data)

channel.basic_publish(exchange='s5', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()