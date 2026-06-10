import socket


HOST = "127.0.0.1"
PORT = 5020
SERVER_PORT = 5021
TOKEN = "12345"


def posalji_serveru(resurs):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, SERVER_PORT))
    client.sendall(resurs.encode("utf-8"))
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

    if len(delovi) != 2 or delovi[0] != TOKEN:
        odgovor = "Pristup odbijen"
    else:
        odgovor = posalji_serveru(delovi[1])

    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
