import socket

# Define the IP address and port number
IP_ADDRESS = '127.0.0.1'
PORT = 12345

# Create a UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the IP address and port number
server_socket.bind((IP_ADDRESS, PORT))

# Wait for a client to connect
print('Waiting for a client to connect...')
data, address = server_socket.recvfrom(1024)
print(f'Received data: {data.decode()} from {address}')

# Send data to the client
message = 'Hello from server!'
server_socket.sendto(message.encode(), address)
print(f'Sent data: {message}')

# Close the socket
server_socket.close()
