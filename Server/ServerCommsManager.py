import logging
import socket
import os
from Dependencies.Constants import *
from concurrent.futures import ThreadPoolExecutor

from Server.Services.FileService import FileService
from Server.Services.UserService import UserService


class ServerClass:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_server_running = True

        self.file_service = FileService()
        self.user_service = UserService()

        self.host_addr = host_addr
        self.server.bind(self.host_addr)

        self.pool = ThreadPoolExecutor(2*os.cpu_count())

        self.server_listen()


    def server_listen(self):
        self.server.listen(100)
        logging.info("Server Listening On", self.host_addr)
        while self.is_server_running:
            client, client_addr = self.server.accept()
            self.pool.submit(self.accept_client_connection, client, client_addr)
        logging.info("Server Closed.")


    def accept_client_connection(self, client, client_addr):
        logging.info("Connected to", client_addr)
        client.send(b"Hello, client!")

        data = client.recv(buffer_size).decode()
        self.parse_message(client, data)

    def parse_message(self, client, message):
        data = message.split(seperator)
        verb = data[0]

        match verb:
            case "GET":
                print("verb = GET")
                self.file_service.send_file(client, data[1])
            case "PUT":
                print("verb = PUT")
                self.user_service.create_user(data[1], data[2])
            case _:
                print("Invalid Verb")

        client.close()


    def server_close(self):
        self.server.close()


if __name__ == "__main__":
    a = ServerClass()
