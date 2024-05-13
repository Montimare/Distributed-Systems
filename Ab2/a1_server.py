import socket
import signal
import sys
import threading

HOST = "localhost"
PORT = 5678


def sig_handler ( sig , frame ) :
    print("Exiting server")
    s.close()
    sys.exit (0)

signal.signal(signal.SIGINT, sig_handler)

def send():
    while True:
        msg = "Server: " + input()
        conn.send(msg.encode())

def receive():
    while True:
        data = conn.recv(1024)
        if not data: 
            continue
        msg = data.decode()
        print(msg)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen()


while True:
    (conn, addr) = s.accept()


    try:
        t1 = threading.Thread(target=send)
        t1.start()
        t2 = threading.Thread(target=receive)
        t2.start()
        t1.join()
        t2.join()

    finally:
        conn.close()


# geklaut von dominic für multithreading

# t1 = threading.Thread(target=server)
# t2 = threading.Thread(target=client)
# t1.start()
# t2.start()

# t1.join()
# t2.join()
