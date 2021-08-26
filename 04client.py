import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ("127.0.0.1", 5555)

client.connect(serverAddress)
message = input()
while message != "":
    client.send(message.encode('utf8'))
    data = client.recv(2048)
    print("Reply from server="+data.decode('utf8'))
    message = input()


socket.close(0)

# socket = IP + PORT + PROTOCOL
