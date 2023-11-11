from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Adiciona suporte a CORS

objetos = [
    {
        'tipo': 'temperatura',
        'sensor': 25.0,
        'Ar condicionado': 22.0,
        'status': True
    },
    {
        'tipo': 'som',
        'sensor': 20.0,
        'Caixa de som': 15,
        'status': True
    },
    {
        'tipo': 'luz',
        'sensor': 'ligado',
        'lâmpada': 'ligada',
        'status': True
    },
]

# Aqui foi para pegar o status de todos os "objetos"
@app.route('/objeto', methods=['GET'])
def obter_status():
    return jsonify(objetos)

# Aqui pega para cada coisa medida
@app.route('/objeto/<tipo>', methods=['GET'])
def obter_objeto(tipo):
    for objeto in objetos:
        if objeto.get('tipo') == tipo:
            return jsonify(objeto)
    return jsonify({'mensagem': 'Objeto não encontrado'}), 404

# Editar
@app.route('/objeto/<tipo>', methods=['PUT'])
def edita_objeto_tipo(tipo):
    tipo_alterado = request.get_json()
    for indice, objeto in enumerate(objetos):
        if objeto.get('tipo') == tipo:
            objetos[indice].update(tipo_alterado)
            return jsonify(objetos[indice])
    return jsonify({'mensagem': 'Objeto não encontrado'}), 404

# Ar condicionado
@app.route('/objetos/temperatura/ar_condicionado', methods=['PUT'])
def editar_ar_condicionado():
    tipo_alterado = request.get_json()
    ar_condicionado = objetos[0]['Ar condicionado']
    ar_condicionado.update(tipo_alterado)
    return jsonify(ar_condicionado)

# Caixa de som
@app.route('/objetos/som/caixa_de_som', methods=['PUT'])
def editar_caixa_de_som():
    tipo_alterado = request.get_json()
    caixa_de_som = objetos[1]['Caixa de som']
    caixa_de_som.update(tipo_alterado)
    return jsonify(caixa_de_som)

# Lâmpada
@app.route('/objetos/luz/lampada', methods=['PUT'])
def editar_lampada():
    tipo_alterado = request.get_json()
    lampada = objetos[2]['lampada']
    lampada.update(tipo_alterado)
    return jsonify(lampada)

if __name__ == '__main__':
    app.run(port=3002, host='localhost', debug=True)
