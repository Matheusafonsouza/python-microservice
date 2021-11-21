import pika
import json

params = pika.URLParameters(
    'amqps://uswndzhq:DT0zKsVmkDKO1GlhfW4Y5NLI-JqV5o_Z@woodpecker.rmq.cloudamqp.com/uswndzhq')

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange='',
        routing_key='admin',
        body=json.dumps(body),
        properties=properties
    )
