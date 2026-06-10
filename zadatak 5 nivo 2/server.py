import socket


HOST = "127.0.0.1"
PORT = 5032


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server radi.")

while True:
    conn, addr = server.accept()
    zahtev = conn.recv(1024).decode("utf-8")

    with open("baza.txt", "a", encoding="utf-8") as fajl:
        fajl.write(zahtev + "\n")

    conn.sendall("Unos potvrdjen".encode("utf-8"))
    conn.close()
