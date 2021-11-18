import pika

params = pika.URLParameters(
    'amqps://uswndzhq:DT0zKsVmkDKO1GlhfW4Y5NLI-JqV5o_Z@woodpecker.rmq.cloudamqp.com/uswndzhq')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming')
channel.start_consuming()
channel.close()
