import pika

class SensorPresenca:
    def __init__(self) -> None:
        pass

    def verificaPresenca(self):
        presenca = input('Tem alguém aí? Digite 1 para sim, 0 para não: ')
        return presenca

# Configurar a conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='presenca_queue')

while True:
    sensor = SensorPresenca()
    presenca = sensor.verificaPresenca()
    print('Presença:', presenca)

    # Publicar a mensagem no RabbitMQ
    channel.basic_publish(exchange='', routing_key='presenca_queue', body=presenca)
    print(f'Mensagem {presenca} publicada na fila')

connection.close()
