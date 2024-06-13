import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while True:
    message = input("Enter your message: ")
    if not message:
        continue
    socket.send(message.encode())
    response = socket.recv()
    current_date = time.ctime()
    print(f"Received request: {response.decode()} - {current_date}")
