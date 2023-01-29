import socket

server_socket = socket.socket()
print("Socket Created")

server_socket.bind(('localhost', 9999)) #IP address, port number
server_socket.listen(3)
print("Waiting for connection ...")

while True:
    client_socket, address = server_socket.accept()
    name = client_socket.recv(1024).decode()
    print("Connected to ", address, name)
    client_socket.send(bytes("Welcome to the house.", "utf-8"))

    client_socket.close()