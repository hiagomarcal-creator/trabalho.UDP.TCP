import sys
from socket import *

serverName = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
serverPort = 1217

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

pergunta = clientSocket.recv(1024).decode()
print(pergunta)
escolha = input()
clientSocket.send(escolha.encode())

# o servidor fecha a conexão depois de responder, então lemos até acabar
resposta = b''
while True:
    pedaco = clientSocket.recv(1024)
    if not pedaco:
        break
    resposta += pedaco

print(resposta.decode())
clientSocket.close()