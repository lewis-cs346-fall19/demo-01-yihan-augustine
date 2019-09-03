# Yihan Mo

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("0.0.0.0", 20350)
sock.connect(addr)
i = 0

for i in range(0,100):
    msg = "This is information send from client\n"
    sock.sendall(msg.encode())
    rec = sock.recv(1024).decode()
    print(rec)


