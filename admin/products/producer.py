import pika

params = pika.URLParameters(
    'amqps://uswndzhq:DT0zKsVmkDKO1GlhfW4Y5NLI-JqV5o_Z@woodpecker.rmq.cloudamqp.com/uswndzhq')

connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
