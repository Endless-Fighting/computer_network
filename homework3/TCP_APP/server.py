# this program references the github of the teacher and CSDN

from socket import *

server_name = "10.132.101.148"
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((server_name, server_port))
server_socket.listen(1)

print("server is ready")

while True:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(1024).decode()
    sentence = sentence[::-1]
    connection_socket.send(sentence.encode())
    connection_socket.close()