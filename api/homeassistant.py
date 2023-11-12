import socket
import grpc
from proto import messages_pb2
from proto import messages_pb2_grpc
from flask_cors import CORS #Route
from flask import Flask, jsonify, request #Route
import pika
import threading
import csv
import json

# Route
app = Flask(__name__)
CORS(app)
# Nome do arquivo JSON
nome_arquivo = 'objs.json'

# Lendo o arquivo JSON como um objeto Python


def process_message(ch, method, properties,body, queue_name):
    
    if queue_name == 'presenca_queue':
        nome_arquivo = 'lampada.json'
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = body.decode('utf-8')
        atributo_desejado = 'lampada'

        if msg == '0':
            objetos.get(atributo_desejado)['status'] = False
        elif msg == '1':
            objetos.get(atributo_desejado)['status'] = True
        # Salvar os dados modificados de volta no arquivo
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)

    elif queue_name == 'temperatura_queue':
        nome_arquivo = 'arcondicionado.json'
        lim = 1.5
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = float(body.decode('utf-8'))
        atributo_desejado = 'Ar condicionado'
        temp = objetos.get(atributo_desejado)['temperatura']
        if msg <= temp-lim:
            objetos.get(atributo_desejado)['status'] = False
        elif msg > temp+lim :
            objetos.get(atributo_desejado)['status'] = True
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)

    elif queue_name == 'audio_queue':
        nome_arquivo = 'caixaSom.json'
        with open(nome_arquivo, 'r') as arquivo:
            objetos = json.load(arquivo)
        msg = float(body.decode('utf-8'))
        atributo_desejado = 'Caixa de som'
        lim = objetos.get(atributo_desejado)['limite']
        print(objetos.get(atributo_desejado)['volume'])
        if msg >= lim:
            v_atual = objetos.get(atributo_desejado)['volume']
            objetos.get(atributo_desejado)['volume'] = v_atual-1

        with open(nome_arquivo, 'w') as arquivo:
            json.dump(objetos, arquivo, indent=2)


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
    @app.route('/objetos', methods=['GET'])
    def obter_status():
        return jsonify(objetos)

#Rota para pegar um "objeto" determinado
    @app.route('/objetos/<string:tipo>', methods=['GET'])
    def obter_objeto(tipo):
        for objeto in objetos:
            if objeto['tipo'] == tipo:
                return jsonify(objeto)
        return jsonify({'mensagem': 'Objeto não encontrado'}), 404

#Rota para alterar um "objeto" determinado
    @app.route('/objetos/<string:tipo>/editar', methods=['PUT'])
    def editar_objeto(tipo):
        dados_recebidos = request.get_json()
        for objeto in objetos:
            if objeto['tipo'] == tipo:
                objeto.update(dados_recebidos)
                return jsonify(objeto)
        return jsonify({'mensagem': 'Objeto não encontrado'}), 404

#Rota para editar o ar condicionado
    @app.route('/objetos/temperatura/ar_condicionado', methods=['PUT'])
    def editar_ar_condicionado():
        dados_recebidos = request.get_json()
        ar_condicionado = objetos[0]['Ar condicionado']
        ar_condicionado.update(dados_recebidos)
        return jsonify(ar_condicionado)

#Rota para editar a caixa de som
    @app.route('/objetos/som/caixa_de_som', methods=['PUT'])
    def editar_caixa_de_som():
        dados_recebidos = request.get_json()
        caixa_de_som = objetos[1]['Caixa de som']
        caixa_de_som.update(dados_recebidos)
        return jsonify(caixa_de_som)

#Rota para editar a Lâmpada
    @app.route('/objetos/luz/lampada', methods=['PUT'])
    def editar_lampada():
        dados_recebidos = request.get_json()
        lampada = objetos[2]['lampada']
        lampada.update(dados_recebidos)
        return jsonify(lampada)
    
    app.run(port=3002, host='localhost', debug=True)
    
    run()
