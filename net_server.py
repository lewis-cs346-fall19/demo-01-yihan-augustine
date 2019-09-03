# Yihan Mo

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("0.0.0.0", 20350)
sock.bind(addr)

sock.listen(5)
while(True):
    (connectedSock, clientAddress) = sock.accept()

while(True):
    msg = sock.recv(1024).decode()
    msg = msg + "Here is what I send back"
    sock.close()

sock.sendall(msg.encode())
