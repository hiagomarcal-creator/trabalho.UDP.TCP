from socket import *
from ferias import PERGUNTA, montar_resposta

serverPort = 1217
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('O servidor UDP está pronto para receber')

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        texto = message.decode()
        if texto == 'INICIAR':
            serverSocket.sendto(PERGUNTA.encode(), clientAddress)
        else:
            print(f'{clientAddress} escolheu: {texto.strip()}')
            serverSocket.sendto(montar_resposta(texto).encode(), clientAddress)
except KeyboardInterrupt:
    print('\nServidor encerrado.')
finally:
    serverSocket.close()