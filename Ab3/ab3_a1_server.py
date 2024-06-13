import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    if not message:
        continue
    current_date = time.ctime()
    print(f"Received request: {message.decode()} - {current_date}")
    user_input = input("Enter your response: ")
    if not user_input:
        continue
    time.sleep(1)
    socket.send(b"World")
