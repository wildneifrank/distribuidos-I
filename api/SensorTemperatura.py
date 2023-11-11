import pika

class SensorTemperatura:
    def __init__(self) -> None:
        pass

    def verificaPresenca(self):
        presenca = input('Tem alguém aí? Digite 1 para sim, 0 para não: ')
        return presenca

# Configurar a conexão RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar uma fila chamada 'presenca_queue'
channel.queue_declare(queue='temperatura_queue')

while True:
    sensor = SensorTemperatura()
    presenca = sensor.verificaPresenca()
    print('Presença:', presenca)

    # Publicar a mensagem no RabbitMQ
    channel.basic_publish(exchange='', routing_key='temperatura_queue', body=presenca)
    print(f'Mensagem {presenca} publicada na fila')

# Fechar a conexão com o RabbitMQ
connection.close()
