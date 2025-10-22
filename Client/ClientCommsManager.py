import math
import socket
import logging

from Client.Services.FileService import FileService
from Dependencies.Constants import *


class ClientClass:
    def __init__(self):
        self.sock = None
        self.file_service = FileService()
        pass

    def connect_to_server(self, host_address=host_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(host_address)
        logging.info('Connected to', host_addr)

        connection_confirmation = self.sock.recv(buffer_size).decode()
        logging.info(connection_confirmation)

    def send_message(self, verb, data, data2=None):
        match verb:
            case "GET":
                logging.debug("Sending: GET")
                self.sock.send(f"{verb}{seperator}{data}".encode())

                self.file_service.receive_file(self, "/Users/yocha/Downloads/")

            case "PUT":
                logging.debug("Sending: PUT")
                self.sock.send(f"{verb}{seperator}{data}{seperator}{data2}".encode())
            case _:
                logging.debug("Invalid Verb")




if __name__ == "__main__":
    client = ClientClass()

    client.connect_to_server(host_addr)

    client.send_message("PUT", "USERNAME", "PASSWORD_HASH")

    client.sock.close()
    client.connect_to_server(host_addr)

    client.send_message("GET", "/Users/yocha/Python Stuff/www/R8.jpg")





    client.sock.close()
