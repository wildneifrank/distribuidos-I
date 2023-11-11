import socket
import grpc
from proto import messages_pb2
from proto import messages_pb2_grpc
import pika
import threading

def process_message(ch, method, properties,body, queue_name):
    print(f"Recebido: {body} de  {queue_name}")
    # Aqui você pode adicionar a lógica de processamento para a mensagem recebida

# Função para consumir mensagens de uma fila específica
def consume_queue(queue_name):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=lambda ch, method, properties, body: process_message(ch, method, properties, body, queue_name), auto_ack=True)

        
    print(f'Aguardando mensagens da fila {queue_name}. Pressione CTRL+C para sair.')
    channel.start_consuming()



def run():
    print("Home Assistant Inicializando...")

    #Conexão Ar Condicionado
    channel_ar = grpc.insecure_channel("localhost:50051")
    stub_ar = messages_pb2_grpc.GatewayStub(channel_ar)
    #Conexão Lâmpada
    channel_lp = grpc.insecure_channel("localhost:50052")
    stub_lp = messages_pb2_grpc.GatewayStub(channel_lp)
    #Conexão Sistema de Som
    channel_ss = grpc.insecure_channel("localhost:50053")
    stub_ss = messages_pb2_grpc.GatewayStub(channel_ss)

    # Criar threads para consumir mensagens de diferentes filas
    thread1 = threading.Thread(target=consume_queue, args=('presenca_queue',))
    thread2 = threading.Thread(target=consume_queue, args=('audio_queue',))
    thread3 = threading.Thread(target=consume_queue, args=('temperatura_queue',))

    # Iniciar as threads
    thread1.start()
    thread2.start()
    thread3.start()




    channel_ar.close()
    channel_lp.close()
    channel_ss.close()

if __name__ == "__main__":
    run()
