import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 9999)) #IPaddress, port number

name = input("Enter your name")
client_socket.send(bytes(name, "utf-8")) #sending in the form of bytes and format "utf-8"
print(client_socket.recv(1024).decode())