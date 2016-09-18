from socket import socket, AF_INET, SOCK_STREAM, sys
serverHost = 'localhost'
serverPort = 50005

message = b'{"name":"ira","comment":"Hello world"}'

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
if len(sys.argv) > 2:
    message = sys.argv[2].encode()

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
sockobj.send(message)
data = sockobj.recv(1024)
print('Client received:', data)

