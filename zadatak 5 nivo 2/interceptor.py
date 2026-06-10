import socket
from datetime import datetime


HOST = "127.0.0.1"
PORT = 5030
MIDDLEWARE_PORT = 5031


def posalji_middlewareu(zahtev):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, MIDDLEWARE_PORT))
    client.sendall(zahtev.encode("utf-8"))
    odgovor = client.recv(1024).decode("utf-8")
    client.close()
    return odgovor


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Interceptor radi.")

while True:
    conn, addr = server.accept()
    zahtev = conn.recv(1024).decode("utf-8")
    delovi = zahtev.split("|", 1)

    if len(delovi) == 2:
        user_id = delovi[0]
        podatak = delovi[1]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        zahtev = timestamp + "|" + user_id + "|" + podatak
        odgovor = posalji_middlewareu(zahtev)
    else:
        odgovor = "Neispravan zahtev"

    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
