from socket import *
import traceback
from ferias import PERGUNTA, montar_resposta

serverPort = 1217
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor TCP está pronto para receber')

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f'Conexão de {addr}')
        with connectionSocket:
            try:
                connectionSocket.send(PERGUNTA.encode())
                print('pergunta enviada')
                escolha = connectionSocket.recv(1024).decode()
                print(f'recebido: {escolha!r}')
                connectionSocket.send(montar_resposta(escolha).encode())
                print('resposta enviada')
            except Exception:
                traceback.print_exc()
except KeyboardInterrupt:
    print('\nServidor encerrado.')
finally:
    serverSocket.close()