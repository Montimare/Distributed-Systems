from email.policy import default
import threading
import time
import zmq

context = zmq.Context()
# set up the subscriber
socket_sub = context.socket(zmq.SUB)
socket_sub.connect("tcp://localhost:5555")

# PUSH socket
socket_push = context.socket(zmq.PUSH)
socket_push.connect("tcp://localhost:5556")

def send():
    print("Enter a message whenever you want to send something:\nPossible Operations: publish <message>, get_value <key>, set_value <key>")
    while True:
        message = input()
        if not message:
            continue
        message = "username " + message
        socket_push.send(message.encode())
t1 = threading.Thread(target=send)
t1.start()

channel = "channel1"
# channel = input("Enter the channel name: ")
# subscribe
socket_sub.setsockopt_string(zmq.SUBSCRIBE, channel)

while True:
    # message = socket_sub.recv_string()
    # if not message:
    #     continue
    
    response = socket_sub.recv()
    current_date = time.ctime()
    print(f"Received request: {response.decode()} - {current_date}")
