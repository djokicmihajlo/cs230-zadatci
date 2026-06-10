import os
import socket


HOST = "127.0.0.1"
PORT = 5040

serveri = {
    "server1": 5041,
    "server2": 5042,
}


def najbliza_putanja(putanja):
    delovi = putanja.strip("/").split("/")

    while delovi:
        provera = os.path.join(*delovi)

        if os.path.exists(provera):
            return "/" + "/".join(delovi)

        delovi.pop()

    return "/"


def posalji_serveru(putanja, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, port))
    client.sendall(putanja.encode("utf-8"))
    odgovor = client.recv(4096).decode("utf-8")
    client.close()
    return odgovor


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Middleware radi.")

while True:
    conn, addr = server.accept()
    putanja = conn.recv(1024).decode("utf-8")
    delovi = putanja.strip("/").split("/")
    lokalna_putanja = putanja.lstrip("/")

    if delovi and delovi[0] in serveri and os.path.isfile(lokalna_putanja):
        odgovor = posalji_serveru(putanja, serveri[delovi[0]])
    else:
        odgovor = "Fajl ne postoji. Najbliza putanja: " + najbliza_putanja(putanja)

    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
