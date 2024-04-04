import os
import pika
import psycopg2

from psycopg2 import Error


amqp_url = os.environ['AMQP_URL']
url_params = pika.URLParameters(amqp_url)

# Подключение к RabbitMQ
connection = pika.BlockingConnection(url_params)
chan = connection.channel()

# Подключение к PostgreSQL
conn = psycopg2.connect(
        host='db',
        user='app_user',
        password='Qwerty123',
        database='postgres',
        )
conn.autocommit = True
cur = conn.cursor()
chan.queue_declare(queue='random_value', durable=True)


def receive_msg(ch, method, properties, body):
    """Function for a random value from Rabbitmq"""

    try:
        create_table_query = '''CREATE TABLE table_numbers
                                (id SERIAL PRIMARY KEY,
                                value INTEGER NOT NULL);'''
        cur.execute(create_table_query)
        conn.commit()
        print(f'Table was successfully created in PostgreSQL')
        random_value = int(body)
        print(f'Random value this is: {random_value}')
        cur.execute("INSERT INTO table_numbers (value) VALUES (%s)",
                    (random_value,))
        conn.commit()
        print(f'The record has been created: {random_value}')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except (Exception, Error) as error:
        print(f'Error when working with PostgreSQL', error)
    finally:
        if connection:
            cur.close()
            connection.close()
            print(f'Сonnection to PostgreSQL is closed')


chan.basic_qos(prefetch_count=1)
chan.basic_consume(queue='random_value',
                   on_message_callback=receive_msg,)
print(f'Waiting to consume')
chan.start_consuming()
