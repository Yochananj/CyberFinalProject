import math
import socket
import logging

from Client.Services.ClientFileService import FileService
from Dependencies.Constants import *
from Dependencies.VerbDictionary import Verbs


class ClientClass:
    def __init__(self):
        self.sock = None
        self.file_service = FileService()
        self.token = "no_token"
        pass

    def send_message(self, verb: Verbs, data: list):
        self.connect_to_server(host_addr)

        match verb:
            case "SIGN_UP":
                logging.debug("Sending: SIGN_UP")
                message = self.write_message(verb, data)
                self.sock.send(message.encode())

            case "LOG_IN":
                logging.debug("Sending: LOG_IN")
                message = self.write_message(verb, data)
                self.sock.send(message.encode())

            case "DOWNLOAD_FILE":
                logging.debug("Sending: DOWNLOAD_FILE")
                message = self.write_message(verb, data)
                self.sock.send(message.encode())

                self.receive_file(self, "/Users/yocha/Downloads/")

            case _:
                logging.debug("Invalid Verb")

        self.sock.close()

    def connect_to_server(self, host_address=host_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(host_address)
        logging.info('Connected to', host_addr)

    def receive_file(self, client_sock, path_to_save_to, file_name):
        file_size = client_sock.sock.recv(buffer_size).decode()
        logging.info("File size is:", file_size, "bytes")

        finished = False
        index = 0
        file_contents = b""

        while not finished:
            connection_confirmation = client_sock.sock.recv(buffer_size)

            index += 1
            if index % 10 == 0:
                logging.debug(f"received data chunk {index} / {math.ceil(int(file_size) / buffer_size)}")

            if connection_confirmation.endswith(end_flag):
                finished = True
                file_contents += connection_confirmation[:-len(end_flag)]
            else:
                file_contents += connection_confirmation

        logging.info("finished receiving data")

        self.file_service.write_file_to_disk(file_contents, path_to_save_to, file_name)

    def write_message(self, verb, data_parts: list):
        message = verb + seperator + self.token + seperator
        for i in range(len(data_parts) - 1):
            message += data_parts[i] + seperator
        message += data_parts[-1]
        return message

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    client = ClientClass()

    client.connect_to_server(host_addr)

    client.send_message("PUT", "USERNAME", "PASSWORD_HASH")

    client.sock.close()
    client.connect_to_server(host_addr)

    client.send_message("GET", "/Users/yocha/Python Stuff/www/R8.jpg")

    client.sock.close()
