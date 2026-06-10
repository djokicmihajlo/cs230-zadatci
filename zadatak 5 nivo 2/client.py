import socket


HOST = "127.0.0.1"
PORT = 5030


user_id = input("Unesite userId: ")
podatak = input("Unesite podatak: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall((user_id + "|" + podatak).encode("utf-8"))
odgovor = client.recv(1024).decode("utf-8")
client.close()

print(odgovor)
