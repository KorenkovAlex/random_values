import os
import pika
import random


amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

# Подключение к RabbitMQ
connection = pika.BlockingConnection(url_params)
chan = connection.channel()
chan.queue_declare(queue='random_value', durable=True)

"""Publish a random value to the queue"""
random_value = random.randint(1, 98)
chan.basic_publish(exchange='',
                   routing_key='random_value',
                   body=str(random_value),
                   properties=pika.BasicProperties(delivery_mode=2))
print(f'Produced the message random value: {random_value}')

chan.close()
connection.close()
