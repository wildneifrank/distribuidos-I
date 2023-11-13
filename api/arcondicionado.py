from concurrent import futures
import grpc
import sys
import json

sys.path.append('../')
from proto import messages_pb2
from proto import messages_pb2_grpc

class ArCondicionadoController:
    def __init__(self):
        filename = 'jsons/arcondicionado.json'
        with open(filename, 'r') as arquivo:
            objetos = json.load(arquivo)
        self.state = True;
        self.temp = objetos['Ar_condicionado']['temperatura'];

ar_condicionado = ArCondicionadoController() #acho q vai ficar globel pfvr fique

class Gateway(messages_pb2_grpc.GatewayServicer):
    global ar_condicionado
   
    def ligarAr(self, request, context):
        if ar_condicionado.state:
             return messages_pb2.Reply(response=f"Ar Condicionado já está ligado.", status=True)
        else:
            ar_condicionado.state = True
            return messages_pb2.Reply(response=f"Ar Condicionado agora está ligado.", status=True)

    def desligarAr(self, request, context):
        if ar_condicionado.state:
            ar_condicionado.state = False
            return messages_pb2.Reply(response="Ar Condicionado agora está em standby.", status=False)
        else:
            return messages_pb2.Reply(response=f"Ar Condicionado já está em standby.", status=False)
        
    def obterStatusAr(self, request, context):
        if ar_condicionado.state:
            return messages_pb2.Reply(response="Ligado", status=True)
        return messages_pb2.Reply(response="Desligado", status=False)

    def aumentarTemperatura(self, request, context):
        if ar_condicionado.state and ar_condicionado.temp < 27:
            ar_condicionado.temp += 1
            return messages_pb2.Reply(response=f"Temperatura aumentada para {ar_condicionado.temp}ºC", value=ar_condicionado.temp)
        elif ar_condicionado.temp >= 27:
            return messages_pb2.Reply(response=f"Temperatura está no máximo de {ar_condicionado.temp}ºC", value=ar_condicionado.temp)
        else:
            return messages_pb2.Reply(response="Ar Condicionado está desligado. Não é possível aumentar a temperatura.", value=ar_condicionado.temp)

    def diminuirTemperatura(self, request, context):
        if ar_condicionado.state and ar_condicionado.temp > 16.0:
            ar_condicionado.temp -= 1
            return messages_pb2.Reply(response=f"Temperatura diminuida para {ar_condicionado.temp}ºC", value=ar_condicionado.temp)
        elif ar_condicionado.temp <= 16:
            return messages_pb2.Reply(response=f"Temperatura está no mínimo de {ar_condicionado.temp}ºC", value=ar_condicionado.temp)
        else:
            return messages_pb2.Reply(response="O Ar Condicionado está desligado. Não é possível diminuir a temperatura.", value=ar_condicionado.temp)
        
    def obterTemperatura(self, request, context):
        return messages_pb2.Reply(response=str(ar_condicionado.temp), value=ar_condicionado.temp)

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
