import os
import socket


HOST = "127.0.0.1"
PORT = 5011


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server1 radi.")

while True:
    conn, addr = server.accept()
    putanja = conn.recv(1024).decode("utf-8")
    lokalna_putanja = putanja.lstrip("/")

    if os.path.isfile(lokalna_putanja):
        with open(lokalna_putanja, "r", encoding="utf-8") as fajl:
            odgovor = fajl.read()
    else:
        odgovor = "Fajl ne postoji na serveru1."

    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
