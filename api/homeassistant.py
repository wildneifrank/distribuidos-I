import socket
import grpc
import sys

sys.path.append('../')
from proto import messages_pb2
from proto import messages_pb2_grpc

def run():
    print("Home Assistant Inicializando...")

    #Conexão Usuário
    home_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    home_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    home_socket.bind(('127.0.0.1', 50050))
    home_socket.listen(1)
    user, addr = home_socket.accept()
    print("Conectado com o Usuário...")

    #Conexão Ar Condicionado
    channel_ar = grpc.insecure_channel("localhost:50051")
    stub_ar = messages_pb2_grpc.GatewayStub(channel_ar)
    #Conexão Lâmpada
    channel_lp = grpc.insecure_channel("localhost:50052")
    stub_lp = messages_pb2_grpc.GatewayStub(channel_lp)
    #Conexão Sistema de Som
    channel_ss = grpc.insecure_channel("localhost:50053")
    stub_ss = messages_pb2_grpc.GatewayStub(channel_ss)

    while True:
        print('Esperando ação do Usuário...')
        usr = user.recv(1024).decode('utf-8')
        
        if(usr == '11'):
            responseCall = stub_lp.ligarLampada(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '12'):
            responseCall = stub_lp.desligarLampada(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '13'):
            #RabbitMQ sensor lampada
            user.sendall("tamo ajeitando ainda".encode('utf-8'))
            #!!!!!!!
        elif(usr == '21'):
            responseCall = stub_ar.ligarAr(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '22'):
            responseCall = stub_ar.desligarAr(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '23'):
            responseCall = stub_ar.aumentarTemperatura(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '24'):
            responseCall = stub_ar.diminuirTemperatura(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '25'):
            #RabbitMQ sensor arcondicondaor
            user.sendall("tamo ajeitando ainda".encode('utf-8'))
            #!!!!!!!
        elif(usr == '31'):
            responseCall = stub_ss.ligarSom(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '32'):
            responseCall = stub_ss.desligarSom(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '33'):
            responseCall = stub_ss.aumentarVolume(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '34'):
            responseCall = stub_ss.diminuirVolume(messages_pb2.Empty())
            user.sendall(responseCall.response.encode('utf-8'))
        elif(usr == '35'):
            #RabbitMQ sensor syssom
            user.sendall("tamo ajeitando ainda".encode('utf-8'))
            #!!!!!!!
        elif(usr == '40'):
            break
        else:
            user.sendall('acho q buguei kkkkk'.encode('utf-8'))
    
    home_socket.close()
    user.close()
    channel_ar.close()
    #channel_lp.close()
    #channel_ss.close()

if __name__ == "__main__":
    run()
