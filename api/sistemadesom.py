from concurrent import futures
import grpc
import sys

sys.path.append('../')
from proto import messages_pb2
from proto import messages_pb2_grpc

class SistemaSomController:
    def __init__(self):
        self.state = False;
        self.vol = 30; # 20 < volume < 40

sistema_som = SistemaSomController() 

class Gateway(messages_pb2_grpc.GatewayServicer):
    global sistema_som
   
    def ligarSom(self, request, context):
        if sistema_som.state:
             return messages_pb2.Reply(response=f"Sistema de Som já está ligado.", status=True)
        else:
            sistema_som.state = True
            return messages_pb2.Reply(response=f"Sistema de Som agora está ligado.", status=True)

    def desligarSom(self, request, context):
        if sistema_som.state:
            sistema_som.state = False
            return messages_pb2.Reply(response="Sistema de Som agora está em standby.", status=False)
        else:
            return messages_pb2.Reply(response=f"Sistema de Som já está em standby.", status=True)
        
    def obterStatusSom(self, request, context):
        if sistema_som.state:
            return messages_pb2.Reply(response="Ligado", status=True)
        return messages_pb2.Reply(response="Desligado", status=False)

    def aumentarVolume(self, request, context):
        if sistema_som.state and sistema_som.vol < 40:
            sistema_som.vol += 5
            return messages_pb2.Reply(response=f"Volume aumentado para {sistema_som.vol}ºC", value=sistema_som.vol)
        elif sistema_som.vol >= 40:
            return messages_pb2.Reply(response=f"Volume está no máximo de {sistema_som.vol}ºC", value=sistema_som.vol)
        else:
            return messages_pb2.Reply(response="Sistema de Som está desligado. Não é possível aumentar o Volume.", value=sistema_som.vol)

    def diminuirVolume(self, request, context):
        if sistema_som.state and sistema_som.vol > 20:
            sistema_som.vol -= 5
            return messages_pb2.Reply(response=f"Volume diminuido para {sistema_som.vol}ºC", value=sistema_som.vol)
        elif sistema_som.vol <= 20:
            return messages_pb2.Reply(response=f"Volume está no mínimo de {sistema_som.vol}ºC", value=sistema_som.vol)
        else:
            return messages_pb2.Reply(response="O Sistema de Som está desligado. Não é possível diminuir o Volume.", value=sistema_som.vol)
    
    def obterVolume(self, request, context):
        return messages_pb2.Reply(response=str(sistema_som.temp))

def serve():
    port = "50053"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_GatewayServicer_to_server(Gateway(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Sistema de Som iniciado na porta " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    #logging.basicConfig()
    serve()
