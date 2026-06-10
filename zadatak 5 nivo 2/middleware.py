import socket


HOST = "127.0.0.1"
PORT = 5031
SERVER_PORT = 5032


def posalji_serveru(zahtev):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, SERVER_PORT))
    client.sendall(zahtev.encode("utf-8"))
    odgovor = client.recv(1024).decode("utf-8")
    client.close()
    return odgovor


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Middleware radi.")

while True:
    conn, addr = server.accept()
    zahtev = conn.recv(1024).decode("utf-8")
    odgovor = posalji_serveru(zahtev)
    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
