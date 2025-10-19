import socket
import os


class server_class:
    try:
        def __init__(self):
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            self.host_addr = ("127.0.0.1", 8080)
            self.server.bind(self.host_addr)
            self.server_listen()

        def server_listen(self):
            self.server.listen(100)
            print("Server Listening On", self.host_addr)
            self.connect_to_client()


        def connect_to_client(self):
            client, client_addr = self.server.accept()
            print("Connected to", client_addr)
            client.send(b"Hello, client!")

            data = client.recv(1024).decode()
            self.parse_message(client, data)

        def parse_message(self, client, message):
            data = message.split("|||")

            if data[0] == "GET":
                self.send_file(client, data[1])


        def send_file(self, client, path):
            file_size = os.path.getsize(path)
            client.send(str(file_size).encode())
            with open(path, "rb") as file:
                contents = file.read(-1)
                client.sendall(contents)
                client.send("||| END |||".encode())

        def server_close(self):
            self.server.close()

    finally:
        server_close()




a = server_class
