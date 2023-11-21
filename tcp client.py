import socket

IP_ADDRESS = '127.0.0.1'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((IP_ADDRESS, PORT))

message = 'Hello from client!'
client_socket.sendall(message.encode())
print(f'Sent data: {message}')

data = client_socket.recv(1024)
print(f'Received data: {data.decode()}')

client_socket.close()
