# Yihan Mo

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("0.0.0.0", 20350)
sock.bind(addr)
sock.listen(5)
while(True):
    (connectedSock, clientAddress) = sock.accept()
    msg = connectedSock.recv(1024).decode()
    print(msg)
    msg = "Here is what the server send back\n"
    print(msg)
    connectedSock.sendall(msg.encode())
