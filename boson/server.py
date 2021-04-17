import socket

HOST = 'localhost'
PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('aguardando conexão de um cliente.')

conn, ender = s.accept()

print('Conectado em', ender)

while True:
    data = conn.recv(1024)
    if(not data):
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)