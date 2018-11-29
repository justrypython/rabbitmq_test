#encoding:UTF-8
#author:justry

import pika
import sys

credentials = pika.PlainCredentials(username='justry',
                                    password='a123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',
                                                               credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()