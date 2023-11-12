def ligarLampada(stub, filename):
    call = stub.ligarLampada(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('lampada')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def desligarLampada(stub, filename):
    call = stub.desligarLampada(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('lampada')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def obterStatusLampada(stub, filename):
    call = stub.obterStatusLampada(messages_pb2.Empty())
    return call.status

def ligarAr(stub, filename):
    call = stub.ligarAr(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Ar condicionado')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def desligarAr(stub, filename):
    call = stub.desligarAr(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Ar condicionado')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def obterStatusAr(stub, filename):
    call = stub.obterStatusAr(messages_pb2.Empty())
    return call.status

def ligarSom(stub, filename):
    call = stub.ligarSom(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Caixa de som')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def desligarSom(stub, filename):
    call = stub.desligarSom(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Caixa de som')['status'] = call.status
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def obterStatusSom(stub, filename):
    call = stub.obterStatusSom(messages_pb2.Empty())
    return call.status

def aumentarTemperatura(stub, filename):
    call = stub.aumentarTemperatura(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Ar condicionado')['temperatura'] = call.value
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def diminuirTemperatura(stub, filename):
    call = stub.diminuirTemperatura(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Ar condicionado')['temperatura'] = call.value
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def obterTemperatura(stub, filename):
    call = stub.obterTemperatura(messages_pb2.Empty())
    return call.value

def aumentarSom(stub, filename):
    call = stub.aumentarSom(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Caixa de som')['solume'] = call.value
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def diminuirSom(stub, filename):
    call = stub.diminuirSom(messages_pb2.Empty())
    with open(filename, 'r') as arquivo:
        objetos = json.load(arquivo)
        temp = objetos.get('Caixa de som')['solume'] = call.value
    with open(filename, 'w') as arquivo:
        json.dump(objetos, arquivo, indent=2)

def obterSom(stub, filename):
    call = stub.obterSom(messages_pb2.Empty())
    return call.value