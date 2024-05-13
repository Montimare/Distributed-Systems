import socket
import threading

HOST = "localhost"
PORT = 5678

def send():
    while True:
        msg = "Client: " + input()
        s.send(msg.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((HOST, PORT))

    t1 = threading.Thread(target=send)
    t1.start()

    while True:
        data = s.recv(1024)
        if not data: 
            continue
        print(data.decode())

finally:
    s.close()
