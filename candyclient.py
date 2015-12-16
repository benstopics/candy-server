import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('10.230.22.60', 8000))
#clientsocket.send('hello')