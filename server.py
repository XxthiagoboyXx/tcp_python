import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 666

try:
    server.bind((ip, port))
    server.listen(5)
    print("Listening in: {}:{}".format(ip, port))

    (client_socket, address) = server.accept()

    print("Received from: {}".format(address[0]))

    while True:
        data = client_socket.recv(1024)
        print(data)
        client_socket.send('ACK')

        server.close()

except Exception as erro:
    print("Erro", erro)
    server.close()