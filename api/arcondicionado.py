from concurrent import futures
import logging

import grpc
from proto import messages_pb2
from proto import messages_pb2_grpc

class ArCondicionadoController:
    def __init__(self):
        self.state = False;
        self.temp = 20;

ar_condicionado = ArCondicionadoController() #acho q vai ficar globel pfvr fique

class Gateway(messages_pb2_grpc.GatewayServicer):
    global ar_condicionado
   
    def ligarAr(self, request, context):
        if ar_condicionado.state:
             return messages_pb2.Reply(response=f"Ar Condicionado já está ligado.")
        else:
            ar_condicionado.state = True
            return messages_pb2.Reply(response=f"Ar Condicionado agora está ligado.")

    def desligarAr(self, request, context):
        if ar_condicionado.state:
            ar_condicionado.state = False
            return messages_pb2.Reply(response="Ar Condicionado agora está em standby.")
        else:
            return messages_pb2.Reply(response=f"Ar Condicionado já está em standby.")

    def aumentarTemperatura(self, request, context):
        if ar_condicionado.state and ar_condicionado.temp < 27:
            ar_condicionado.temp += 1
            return messages_pb2.Reply(response=f"Temperatura aumentada para {ar_condicionado.temp}ºC")
        elif ar_condicionado.temp >= 27:
            return messages_pb2.Reply(response=f"Temperatura está no máximo de {ar_condicionado.temp}ºC")
        else:
            return messages_pb2.Reply(response="Ar Condicionado está desligado. Não é possível aumentar a temperatura.")

    def diminuirTemperatura(self, request, context):
        if ar_condicionado.state and ar_condicionado.temp > 16:
            ar_condicionado.temp -= 1
            return messages_pb2.Reply(response=f"Temperatura diminuida para {ar_condicionado.temp}ºC")
        elif ar_condicionado.temp <= 16:
            return messages_pb2.Reply(response=f"Temperatura está no mínimo de {ar_condicionado.temp}ºC")
        else:
            return messages_pb2.Reply(response="O Ar Condicionado está desligado. Não é possível diminuir a temperatura.")

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_GatewayServicer_to_server(Gateway(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Ar-condicionado iniciado na porta " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    #logging.basicConfig()
    serve()
