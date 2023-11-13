import socket

def operation(socket, act1, act2):
    #Manda ação pro Home Assistant
    socket.sendall(f"{act1}{act2}".encode('utf-8'))
    #Recebe a resposta do Home Assistent
    response = socket.recv(1024).decode('utf-8')
    print('\n' + response)

def init_client():
    print('Bem vindo ao Alexo Rabbit')

    #Conexão Home Assistant
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 50050))
    
    while(True):
        print('\nDigite o número do objeto que deseja manipular')
        for i in range(len(obj)):
            print(i+1, '-', obj[i])
        acao1 = input()

        if acao1 == '1':
            print('\nLista de ações:')
            for i in range(len(acoes_lp)):
                print(i+1, '-', acoes_lp[i])
            acao2 = input('Digite o número da ação que deseja tomar:')
            if acao2 == '1' or '2' or '3':
                operation(client, acao1, acao2)
            else:
                print('opção inválida')

        elif acao1 == '2':
            print('\nLista de ações:')
            for i in range(len(acoes_ac)):
                print(i+1, '-', acoes_ac[i])
            acao2 = input('Digite o número da ação que deseja tomar:')
            if acao2 == '1' or '2' or '3' or '4' or '5':
                operation(client, acao1, acao2)
            else:
                print('opção inválida')

        elif acao1 == '3':
            print('\nLista de ações:')
            for i in range(len(acoes_ss)):
                print(i+1, '-', acoes_ss[i])
            acao2 = input('Digite o número da ação que deseja tomar:')
            if acao2 == '1' or '2' or '3' or '4' or '5':
                operation(client, acao1, acao2)
            else:
                print('opção inválida')  
                
        elif acao1 == '4':
            acao2 = 0
            operation(client, acao1, acao2)
            break
    client.close()     

obj = [
    'Lampada',
    'Ar condicionado',
    'Sistema de Som',
    'Sair do programa'
]
acoes_lp=[ 
    'Ligar',
    'Desligar a lampada',
    'Status da lampada'
]
acoes_ac = [
    'Ligar',
    'Desligar',
    'Aumentar temperatura',
    'Baixar temperatura',
    'Status do ar-condicionado'
]
acoes_ss = [
    'Ligar',
    'Desligar',
    'Aumentar volume',
    'Baixar volume',
    'Status do sistema de som'
]

if __name__ == "__main__":
    init_client()