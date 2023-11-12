import grpc
import sys

sys.path.append('../')
from proto import messages_pb2
from proto import messages_pb2_grpc
from flask_cors import CORS #Route
from flask import Flask, jsonify, request #Route
import pika
import threading
import json

# Route
app = Flask(__name__)
CORS(app)
# Nome do arquivo JSON
nome_arquivo = 'objs.json'

# Lendo o arquivo JSON como um objeto Python

def process_message(ch, method, properties,body, queue_name,stub):
    
    if queue_name == 'presenca_queue':
        nome_arquivo = 'jsons/lampada.json'
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = body.decode('utf-8')
        atributo_desejado = 'lampada'

        if msg == '0':
            responseCall = stub.desligarLampada(messages_pb2.Empty())
            objetos.get(atributo_desejado)['status'] = False
        elif msg == '1':
            responseCall = stub.ligarLampada(messages_pb2.Empty())
            objetos.get(atributo_desejado)['status'] = True
        # Salvar os dados modificados de volta no arquivo
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)

    elif queue_name == 'temperatura_queue':
        nome_arquivo = 'jsons/arcondicionado.json'
        lim = 1.5
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = float(body.decode('utf-8'))
        atributo_desejado = 'Ar_condicionado'
        temp = objetos.get(atributo_desejado)['temperatura']
        if msg <= temp-lim:
            objetos.get(atributo_desejado)['status'] = False
            responseCall = stub.desligarAr(messages_pb2.Empty())
        elif msg > temp+lim :
            responseCall = stub.ligarAr(messages_pb2.Empty())
            objetos.get(atributo_desejado)['status'] = True
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)

    elif queue_name == 'audio_queue':
        nome_arquivo = 'jsons/caixaSom.json'
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = float(body.decode('utf-8'))
        atributo_desejado = 'Caixa_de_som'

        lim = objetos.get(atributo_desejado)['limite']
        if msg >= lim:
            v_atual = objetos.get(atributo_desejado)['volume']
            objetos.get(atributo_desejado)['volume'] = v_atual-1
            stub.diminuirVolume(messages_pb2.Empty())

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)

    # Aqui você pode adicionar a lógica de processamento para a mensagem recebida

# Função para consumir mensagens de uma fila específica
def consume_queue(queue_name, stub):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=lambda ch, method, properties, body: process_message(ch, method, properties, body, queue_name, stub), auto_ack=True)
   
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
    thread1 = threading.Thread(target=consume_queue, args=('presenca_queue',stub_lp,))
    thread2 = threading.Thread(target=consume_queue, args=('audio_queue',stub_ss,))
    thread3 = threading.Thread(target=consume_queue, args=('temperatura_queue',stub_ar,))

    # Iniciar as threads
    thread1.start()
    thread2.start()
    thread3.start()
    
## Rotas
""" @app.route('/objetos', methods=['GET'])
def obter_status():
    return jsonify(objetos)
"""
#Rota para pegar um "objeto" determinado
@app.route('/objetos/<string:tipo>', methods=['GET'])
def obter_objeto(tipo):
    if(tipo == 'lampada'):
        with open('jsons/lampada.json', 'r') as arquivo:
            objeto = json.load(arquivo)
        return jsonify(objeto)
    elif(tipo == 'caixaSom'):
        with open('jsons/caixaSom.json', 'r') as arquivo:
            objeto = json.load(arquivo)
        return jsonify(objeto)
    elif(tipo == 'arcondicionado'):
        with open('jsons/arcondicionado.json', 'r') as arquivo:
            objeto = json.load(arquivo)
        return jsonify(objeto)
    return jsonify({'mensagem': 'Objeto não encontrado'}), 404


#Ar condicionado
@app.route('/objetos/temperatura/aumentar', methods=['GET'])
def aumentar_temp():
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.aumentarTemperatura(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/temperatura/diminuir', methods=['GET'])
def diminuir_temp():
    try:

        with grpc.insecure_channel('localhost:50051') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.diminuirTemperatura(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/arCond/ligar', methods=['GET'])
def ligar_arCond():
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.ligarAr(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/arCond/desligar', methods=['GET'])
def desligar_arCond():
    try:
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.desligarAr(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

#Som
@app.route('/objetos/som/aumentar', methods=['GET'])
def aumentar_som():
    try:
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.aumentarSom(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/som/diminuir', methods=['GET'])
def diminuir_som():
    try:
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.diminuirSom(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/caixaSom/ligar', methods=['GET'])
def ligar_caixaSom():
    try:
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.ligarSom(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/caixaSom/desligar', methods=['GET'])
def desligar_caixaSom(): 
    try:
        with grpc.insecure_channel('localhost:50053') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.desligarSom(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})           

#Lâmpada
@app.route('/objetos/lampada/ligar', methods=['GET'])
def ligar_lampada():
    try:
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.ligarLampada(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/objetos/lampada/desligar', methods=['GET'])
def desligar_lampada():
    try:
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = messages_pb2_grpc.GatewayStub(channel)
            
            response = stub.desligarLampada(messages_pb2.Empty())
            
            return jsonify({"message": response.response})
    except Exception as e:
        return jsonify({"error": str(e)})
run()
app.run(port=3002, host='localhost', debug=True)
