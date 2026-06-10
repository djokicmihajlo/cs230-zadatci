import socket


HOST = "127.0.0.1"
PORT = 5020


token = input("Unesite token: ")
resurs = input("Unesite resurs: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall((token + "|" + resurs).encode("utf-8"))
odgovor = client.recv(1024).decode("utf-8")
client.close()

print(odgovor)
