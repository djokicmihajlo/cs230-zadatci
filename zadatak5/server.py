import socket


HOST = "127.0.0.1"
PORT = 5021

resursi = {
    "studenti": "Marko, Ana, Jovan",
    "ocene": "10, 9, 8",
    "raspored": "Ponedeljak 10:00",
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server radi.")

while True:
    conn, addr = server.accept()
    resurs = conn.recv(1024).decode("utf-8")
    odgovor = resursi.get(resurs, "Resurs ne postoji.")
    conn.sendall(odgovor.encode("utf-8"))
    conn.close()
