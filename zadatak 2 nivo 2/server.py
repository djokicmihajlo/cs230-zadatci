import socket


HOST = "127.0.0.1"
PORT = 5003


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print("Server je pokrenut.")

conn, addr = server.accept()
print("Klijent se povezao.")

while True:
    poruka = conn.recv(1024).decode("utf-8")

    if not poruka:
        break

    with open("client_log.txt", "a", encoding="utf-8") as fajl:
        fajl.write(poruka + "\n")

    if poruka == "end":
        break

    odgovor = " ".join(poruka.split()[::-1])
    conn.sendall(odgovor.encode("utf-8"))

conn.close()
server.close()
print("Server je zavrsio rad.")
