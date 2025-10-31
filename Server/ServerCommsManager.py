import logging
import socket
import os
from Dependencies.Constants import *
from concurrent.futures import ThreadPoolExecutor
from Server.Services.ServerFileService import FileService
from Server.Services.TokensService import TokensService
from Server.Services.UserService import UserService


class ServerClass:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.is_server_running = True

        self.file_service = FileService()
        self.user_service = UserService()
        self.token_service = TokensService()

        self.host_addr = host_addr
        self.server.bind(self.host_addr)

        self.pool = ThreadPoolExecutor(2*os.cpu_count())

        self.server_listen()


    def server_listen(self):
        self.server.listen(100)
        logging.info(str("Server Listening On", self.host_addr))
        while self.is_server_running:
            client, client_addr = self.server.accept()
            self.pool.submit(self.accept_client_connection, client, client_addr)
        logging.info("Server Closed.")


    def accept_client_connection(self, client, client_addr):
        logging.info(str("Connected to", client_addr))

        data = client.recv(buffer_size).decode()
        self.parse_message(client, data)

    def parse_message(self, client, message):
        verb = message.split(seperator)[0]
        client_token = message.split(seperator)[1]
        data = message.split(seperator)[2, 0]

        is_token_valid = self.token_service.is_token_valid(client_token)

        match verb:
            case "SIGN_UP":
                print("verb = SING_UP")
                self.user_service.create_user(data[1], data[2])

            case "LOG_IN":
                print("verb = LOG_IN")
                pass

            case "DOWNLOAD_FILE":
                if is_token_valid:
                    print("verb = DOWNLOAD_FILE")
                    self.send_file(client, data)
                else:
                    response = self.write_message("ERROR", client_token, "INVALID_TOKEN")
                    self.respond_to_client(client, response)
            case _:
                print("Invalid Verb")


    def respond_to_client(self, client, message):
        client.close()

    def send_file(self, client, path):                      # to be deprecated
        file_size = self.file_service.get_file_size(path)
        client.send(str(file_size).encode())
        contents = self.file_service.get_file_contents(path)
        client.sendall(contents)
        client.send(end_flag)

    def write_message(self, success, token, error_code=None):
        message = success + seperator + token
        if error_code:
            message += seperator + error_code
        return message


    def server_close(self):
        self.server.close()
        self.is_server_running = False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    a = ServerClass()
