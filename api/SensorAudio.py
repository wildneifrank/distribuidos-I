import pika

class SensorAudio:
    def __init__(self) -> None:
        pass

    def verificaAudio(self):
        Audio = input('Tem alguém aí? Digite 1 para sim, 0 para não: ')
        return Audio

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

# Fechar a conexão com o RabbitMQ
connection.close()
