import socket

# Set the host and port for the server
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Receive data from the client
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if len(data)>0:
        print(f"Received message: {data}")
    
# Close the connection
client_socket.close()
server_socket.close()
