#!/usr/bin/env python
import pika
import random
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


while(True):
    n = random.randint(1,1000)
    t = random.randint(1,5)
    for x in range (n):
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print (n)
        print(" [x] Sent!'")
    print("sleeping for " + str(t))
    time.sleep(t)
else:
    connection.close()
