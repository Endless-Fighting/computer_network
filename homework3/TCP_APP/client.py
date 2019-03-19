# this program references the github of the teacher and CSDN

from socket import *

server_name = "10.132.101.148"
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = "hello computer network"
client_socket.send(sentence.encode())

reversed_sentence = client_socket.recv(1024)
print("reversed sentence:", reversed_sentence.decode())

client_socket.close()