import socket

HOST = 'localhost'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Ola, mundo!'))
data = s.recv(1024)

print('Mensagem ecoada: ', data.decode())