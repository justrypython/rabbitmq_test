#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials(username='justry',
                                    password='a123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent %r" % message)
connection.close()