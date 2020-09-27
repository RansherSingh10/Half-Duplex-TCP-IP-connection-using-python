import socket

server_name = 'localhost'
server_port = 5000
client_socket = socket.socket()
client_socket.connect((server_name,server_port))

while True:
  sentence = input(">> ")
  client_socket.send(sentence.encode())
  message = client_socket.recv(2048)
  print (">> ", message.decode())
  if(sentence == 'quit'):
    client_socket.close()