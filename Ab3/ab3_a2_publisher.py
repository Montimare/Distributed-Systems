import time
import zmq

CHANNEL = "channel1"

context = zmq.Context()
# Publisher socket
socket_pub = context.socket(zmq.PUB)
socket_pub.bind("tcp://*:5555")

# response - request sockets didnt work cause you need to answer a request with a response, otherwise breaks 
# PULL socket
socket_pull = context.socket(zmq.PULL)
socket_pull.bind("tcp://localhost:5556")

while True:
    
    message = socket_pull.recv().decode()
    if not message:
        continue
    current_date = time.ctime()
    print(f"Received request: {message} - {current_date}")

    # message = input("Enter your message: ")
    # if not message:
    #     continue

    socket_pub.send_string(f"{CHANNEL} {message}")
