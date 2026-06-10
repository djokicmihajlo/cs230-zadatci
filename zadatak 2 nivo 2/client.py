import socket


HOST = "127.0.0.1"
PORT = 5003


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    poruka = input("Unesite poruku: ")
    client.sendall(poruka.encode("utf-8"))

    if poruka == "end":
        break

    odgovor = client.recv(1024).decode("utf-8")
    print("Server:", odgovor)

client.close()
