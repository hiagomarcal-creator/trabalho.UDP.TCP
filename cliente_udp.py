import sys
from socket import *

serverName = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
serverPort = 1217

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

try:
    clientSocket.sendto('INICIAR'.encode(), (serverName, serverPort))
    pergunta, _ = clientSocket.recvfrom(2048)

    escolha = input(pergunta.decode())
    clientSocket.sendto(escolha.encode(), (serverName, serverPort))

    resposta, _ = clientSocket.recvfrom(4096)
    print(resposta.decode())
except timeout:
    print('O servidor não respondeu a tempo.')
finally:
    clientSocket.close()