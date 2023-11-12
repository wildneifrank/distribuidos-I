import pika
import time
import random

class SensorAudio:
    def __init__(self) -> None:
        pass

    def verificaAudio(self):
        Audio = random.randint(0, 90)
        return str(Audio)

# Configurar a conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila chamada 'Audio_queue'
channel.queue_declare(queue='Audio_queue')

while True:
    sensor = SensorAudio()
    Audio = sensor.verificaAudio()
    print('Presença:', Audio)

    # Publicar a mensagem no RabbitMQ
    channel.basic_publish(exchange='', routing_key='audio_queue', body=Audio)
    print(f'Mensagem {Audio} publicada na fila')
    time.sleep(10)

# Fechar a conexão com o RabbitMQ
connection.close()
