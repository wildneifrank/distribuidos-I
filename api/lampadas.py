from concurrent import futures
import logging

import grpc
from proto import messages_pb2
from proto import messages_pb2_grpc

class LampadaController:
    def __init__(self):
        self.state = False;

lampada = LampadaController()

class Gateway(messages_pb2_grpc.GatewayServicer):
    global lampada

    def ligarLampada(self, request, context):
        if lampada.state:
             return messages_pb2.Reply(response=f"Lâmpada já está ligada.")
        else:
            lampada.state = True
            return messages_pb2.Reply(response=f"Lâmpada agora está ligada.")

    def desligarLampada(self, request, context):
        if lampada.state:
            lampada.state = False
            return messages_pb2.Reply(response="Lâmpada agora está em standby.")
        else:
            return messages_pb2.Reply(response=f"Lâmpada já está em standby.")

def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_GatewayServicer_to_server(Gateway(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Lâmpada iniciada na porta  " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    #logging.basicConfig()
    serve()