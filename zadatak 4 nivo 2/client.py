import socket


HOST = "127.0.0.1"
PORT = 5010


putanja = input("Unesite putanju: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(putanja.encode("utf-8"))
odgovor = client.recv(4096).decode("utf-8")
client.close()

print(odgovor)
