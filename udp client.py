import socket

# Define the IP address and port number
IP_ADDRESS = '127.0.0.1'
PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
message = 'Hello from client!'
client_socket.sendto(message.encode(), (IP_ADDRESS, PORT))
print(f'Sent data: {message}')

# Receive data from the server
data, address = client_socket.recvfrom(1024)
print(f'Received data: {data.decode()}')

# Close the socket
client_socket.close()
