import os
import socket


HOST = "127.0.0.1"
PORT = 5004


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server1 ceka Server2.")

conn, addr = server.accept()
vreme_server2 = float(conn.recv(1024).decode("utf-8"))
vreme_server1 = os.path.getmtime("server1/data.txt")

if vreme_server1 > vreme_server2:
    print("Server1 ima noviju verziju")
elif vreme_server1 < vreme_server2:
    print("Server2 ima noviju verziju")
else:
    print("Fajlovi su sinhronizovani")

conn.close()
server.close()
