import pika
import time

class SensorPresenca:
    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='presenca_queue')

    def verificaPresenca(self):
        presenca = input('Tem alguém aí? Digite 1 para sim, 0 para não: ')
        return presenca

    def enviarPresenca(self, presenca):
        self.channel.basic_publish(exchange='', routing_key='presenca_queue', body=presenca)
        print(f'Mensagem {presenca} publicada na fila')

    def fecharConexao(self):
        self.connection.close()

sensor = SensorPresenca()

while True:
    presenca = sensor.verificaPresenca()
    sensor.enviarPresenca(presenca)
    time.sleep(5)  # Publica a cada 5 segundos

sensor.fecharConexao()
