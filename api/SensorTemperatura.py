import pika
import time
import random

class SensorTemperatura:
    def __init__(self) -> None:
        pass

    def verificaTemperatura(self):
        Temperatura = random.randint(0, 50)
        return str(Temperatura)

# Configurar a conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila chamada 'Temperatura_queue'
channel.queue_declare(queue='temperatura_queue')

while True:
    sensor = SensorTemperatura()
    Temperatura = sensor.verificaTemperatura()
    print('Presença:', Temperatura)

    # Publicar a mensagem no RabbitMQ
    channel.basic_publish(exchange='', routing_key='temperatura_queue', body=Temperatura)
    print(f'Mensagem {Temperatura} publicada na fila')
    time.sleep(5)

# Fechar a conexão com o RabbitMQ
connection.close()
