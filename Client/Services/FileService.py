import logging
import math
import os

from Dependencies.Constants import buffer_size, end_flag


class FileService:
    def __init__(self):
        pass

    def receive_file(self, client, path_to_save_to):
        file_size = client.sock.recv(buffer_size).decode()
        logging.info("File size is:", file_size, "bytes")

        finished = False
        index = 0
        file_contents = b""

        while not finished:
            connection_confirmation = client.sock.recv(buffer_size)

            index += 1
            logging.debug("received data", index, "/", math.ceil(int(file_size) / buffer_size))

            if connection_confirmation.endswith(end_flag):
                finished = True
                file_contents += connection_confirmation[:-len(end_flag)]
            else:
                file_contents += connection_confirmation

        logging.info("finished receiving data")

        path_for_new_file = path_to_save_to
        with open(f"{path_for_new_file}R8.jpg", 'wb') as file:
            file.write(file_contents)

        logging.info("finished writing data to file")