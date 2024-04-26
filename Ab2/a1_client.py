import socket

HOST = "localhost"
PORT = 5678

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.connect((HOST, PORT))
    msg = "Hello Server!"
    s.send(msg.encode())
    data = s.recv(1024)
    print(data.decode())

finally:
    s.close()