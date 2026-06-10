import os
import socket


HOST = "127.0.0.1"
PORT = 5004


vreme = os.path.getmtime("server2/data.txt")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(str(vreme).encode("utf-8"))
client.close()

print("Server2 je poslao vreme izmene.")
