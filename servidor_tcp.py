from socket import *
from ferias import PERGUNTA, montar_resposta

serverPort = 1217
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor TCP está pronto para receber')

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        with connectionSocket:
            try:
                connectionSocket.send(PERGUNTA.encode())
                escolha = connectionSocket.recv(1024).decode()
                print(f'{addr} escolheu: {escolha.strip()}')
                connectionSocket.send(montar_resposta(escolha).encode())
            except OSError as erro:
                print(f'Erro com o cliente {addr}: {erro}')
except KeyboardInterrupt:
    print('\nServidor encerrado.')
finally:
    serverSocket.close()