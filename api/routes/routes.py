from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Adiciona suporte a CORS

objetos = [
    {
        'tipo': 'temperatura',
        'sensor': 25.0,
        'Ar condicionado': {
            'status': 'ligado',
            'temperatura': 22.0
        },
        'status': True
    },
    {
        'tipo': 'som',
        'sensor': 50.0,
        'Caixa de som': {
            'status': 'ligado',
            'volume': 15
        },
        'status': True
    },
    {
        'tipo': 'luz',
        'sensor': 'ligado',
        'lampada': {
            'status': 'ligada'
        },
        'status': True
    }
]

#Rota para pegar os status de todos os "objetos"
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

if __name__ == '__main__':
    app.run(port=3002, host='localhost', debug=True)
