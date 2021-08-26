import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ("127.0.0.1", 5555)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
server.bind(serverAddress)

server.listen(3)
print("server listening....")

client, address = server.accept()
print(f"connected to {address}")
data = client.recv(2048)
while data.decode('utf8') != "":
    print("client sent:"+data.decode("utf-8"))
    client.send(data)
    data = client.recv(2048)

server.close()
