import socket
import sys
import time

s = socket.socket()

host = socket.gethostname()
print("Server Will Start on host", host)
port = 2020
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("server is waiting")
s.listen(1)

conn, addr = s.accept()

print(addr, "Has connected to server and is now online")

print("")


while True:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message has been sent")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client:", incoming_message)
    print("")