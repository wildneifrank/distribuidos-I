import socket
import grpc
from proto import messages_pb2
from proto import messages_pb2_grpc
import pika

def conectarRabbitMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='presenca_queue')
    return channel

def callback(ch, method, properties, body):
    print(f"Recebeu uma mensagem: {body}")

def run():
    print("Home Assistant Inicializando...")

    # Conexão com RabbitMQ
    channel = conectarRabbitMQ()
    channel.basic_consume(queue='presenca_queue', on_message_callback=callback, auto_ack=True)

    while True:
        channel.start_consuming()

if __name__ == "__main__":
    run()
