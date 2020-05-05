import _pickle as pickle  # for faster serialization
from _thread import *
from socket import *

HOST = "172.17.177.158"
PORT = 8999

connections = 0

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except error as e:
    print(str(e))
try:
    s.listen(4)  # max. 4 users in queue
except error as e:
    print(str(e))
print("Waiting for a connection")


def threaded_client(connection, my_id):  # player = id of a player
    global connections

    while True:
        try:
            data = connection.recv(2048)
            message = pickle.loads(data)

            print(f"Message from {my_id}: {message}")

        except Exception as e:
            print(e)
            break
    # disconneted
    try:
        print(f"Connection {my_id} Close")
        connections -= 1
        my_id -= 1
        connection.close()

    except Exception as e:
        print(e)


while True:  # continuously looking 4 connection
    client, addr = s.accept()
    print(f"Connection from {addr} has been established. ID = {connections}.")
    start_new_thread(threaded_client, (client, connections))
    connections += 1
