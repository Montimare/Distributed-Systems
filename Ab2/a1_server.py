import socket
import signal
import sys

HOST = "localhost"
PORT = 5678

def sig_handler ( sig , frame ) :
    print("Exiting server")
    s.close()
    sys.exit (0)

signal.signal(signal.SIGINT, sig_handler)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()
while True:
    (conn, addr) = s.accept()

    try:
        while True:
            data = conn.recv(1024)
            if not data: 
                break
            msg = data.decode()
            print(msg)
            msg = msg + "<server was here>"
            conn.send(msg.encode())

    finally:
        conn.close()