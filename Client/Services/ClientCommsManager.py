import math
import socket
import logging
import time

from Client.Services.ClientFileService import FileService
from Dependencies.Constants import *
from Dependencies.VerbDictionary import Verbs


class ClientClass:
    def __init__(self):
        self.sock: socket.socket = None
        self.file_service = FileService()
        self.token = "no_token"
        pass

    def send_message(self, verb: Verbs, data: list):
        logging.info("Sending Message")
        self.connect_to_server(host_addr)

        message = ""
        receiving_byte_data = False

        match verb:
            case Verbs.SIGN_UP:
                logging.debug("Sending: SIGN_UP")
                message = self.write_message(verb, data)

            case Verbs.LOG_IN:
                logging.debug("Sending: LOG_IN")
                message = self.write_message(verb, data)

            case Verbs.DOWNLOAD_FILE:
                logging.debug("Sending: DOWNLOAD_FILE")
                message = self.write_message(verb, data)

            case Verbs.GET_FILES_LIST:
                logging.debug("Sending: GET_FILES_LIST")
                message = self.write_message(verb, data)

            case _:
                logging.debug("Invalid Verb")

        self.sock.send(message.encode())
        logging.debug(f"Sent Message: {message} \n waiting for response. \n")

        a,b =  self.receive_response(receiving_byte_data)
        return a,b

    def receive_response(self, is_byte_data):
        time.sleep(0.5)
        status = self.sock.recv(buffer_size).decode()

        logging.debug(f"Received and decoded: {status}")

        status_parts = status.split(seperator)

        self.token = status_parts[1]
        logging.debug(f"Saved Token: {self.token}")


        if status_parts[0] == "ERROR":
            logging.debug("Error Occurred")
            logging.debug(f"Error Code: {status_parts[2]}")
            return status_parts[0], status_parts[2]

        logging.debug("Request Successful")

        to_return_data = ""

        if len(status_parts) == 3 and status_parts[2] == "SENDING_DATA":
            logging.debug("Receiving Data")
            to_return_data = self.receive_data(is_byte_data)
            logging.debug(f"Received Data: {to_return_data}, now splitting.")
            to_return_data = to_return_data.split(seperator)

        # self.sock.shutdown(socket.SHUT_RDWR)
        # logging.debug("Connection Closed")

        if len(to_return_data) != 0: return status_parts[0], to_return_data

        return status_parts[0], None

    def connect_to_server(self, host_address=host_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(host_address)
        logging.info(('Connected to', host_addr))

    def write_message(self, verb: Verbs, data_parts: list):
        logging.debug(f"Writing Message: {verb}, {data_parts[0:len(data_parts)]}")
        message = verb.value + seperator + self.token + seperator
        logging.debug(f"Current Message: {message}")
        for i in range(len(data_parts) - 1):
            message += data_parts[i] + seperator
            logging.debug(f"Current Message: {message}, index: {i}")
        message += data_parts[-1]
        logging.debug(f"Final Message: {message}")
        return message

    def receive_file(self):
        file_size = self.sock.recv(buffer_size).decode()
        logging.info(f"File size is: {file_size} bytes")

        file_contents = self.receive_data(file_size)

        return file_contents

    def receive_data(self, is_byte_data=False, file_size=None):
        finished = False
        index = 0
        if is_byte_data:
            received_data = b""
        else:
            received_data = ""

        logging.debug("Initializing data receiving")

        while not finished:
            data_chunk = self.sock.recv(buffer_size)

            index += 1
            if index % 10 == 0 and file_size:
                logging.debug(f"received data chunk {index} / {math.ceil(int(file_size) / buffer_size)}")

            if data_chunk.endswith(end_flag):
                finished = True
                if is_byte_data: received_data += data_chunk[:-(len(seperator)+len(end_flag))]
                else: received_data += data_chunk[:-(len(seperator)+len(end_flag))].decode()
            else:
                if is_byte_data: received_data += data_chunk
                else: received_data += data_chunk.decode()

        logging.info(f"finished receiving data: {received_data}, {type(received_data)}")


        return received_data

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    client = ClientClass()

    client.send_message(Verbs.LOG_IN, ["USERNAME", "PASSWORD_HASH"])

    client.sock.close()
