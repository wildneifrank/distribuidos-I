import pika
import time
import random

class SensorPresenca:
    def __init__(self) -> None:
        pass

    def verificaPresenca(self):
        presenca = random.randint(0, 1)
        return str(presenca)

# Configurar a conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila chamada 'presenca_queue'
channel.queue_declare(queue='presenca_queue')

while True:
    sensor = SensorPresenca()
    presenca = sensor.verificaPresenca()
    print('Presença:', presenca)

    # Publicar a mensagem no RabbitMQ
    channel.basic_publish(exchange='', routing_key='presenca_queue', body=presenca)
    print(f'Mensagem {presenca} publicada na fila')
    time.sleep(1)

# Fechar a conexão com o RabbitMQ
connection.close()
