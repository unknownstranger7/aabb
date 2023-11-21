import socket

IP_ADDRESS = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP_ADDRESS, PORT))

server_socket.listen()

print('Waiting for a client to connect...')
client_socket, client_address = server_socket.accept()
print(f'Client connected from {client_address}')

data = client_socket.recv(1024)
print(f'Received data: {data.decode()}')

message = 'Hello from server!'
client_socket.sendall(message.encode())
print(f'Sent data: {message}')

client_socket.close()
server_socket.close()
