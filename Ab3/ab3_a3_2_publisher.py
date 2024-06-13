import time
import zmq

CHANNEL = "channel1"
dict = {}

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

    user,wanted_operation,message = message.split(" ",maxsplit=2)
    print(f"User: {user} wanted to: {wanted_operation} the message: {message}")

    if wanted_operation == "publish":
        socket_pub.send_string(f"{CHANNEL} User: {user} {message}")
    elif wanted_operation == "get_value":
        socket_pub.send_string(f"{CHANNEL} {dict[message]}")
    elif wanted_operation == "set_value":
        message = message.split(" ", maxsplit=1)
        dict[message[0]] = message[1]
    else:
        print(dict)


    # socket_pub.send_string(f"{CHANNEL} {message}")


# gerade so alles implementiert was gefragt war, aber keine lust error handling und private answer einzurichten