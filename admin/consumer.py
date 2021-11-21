import pika
import json
from products.models import Product

params = pika.URLParameters(
    'amqps://uswndzhq:DT0zKsVmkDKO1GlhfW4Y5NLI-JqV5o_Z@woodpecker.rmq.cloudamqp.com/uswndzhq')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    pk = json.loads(body)

    product = Product.objects.get(pk=pk)
    product.ikes = product.like + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()
channel.close()
