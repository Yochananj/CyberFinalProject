import logging
import math
import os

from Dependencies.Constants import buffer_size, end_flag


class FileService:
    def __init__(self):
        pass


    def write_file_to_disk(self, file_contents, path_to_save_to, file_name):
        os.makedirs(path_to_save_to)
        with open(os.path.join(path_to_save_to, file_name), "wb") as file:
            file.write(file_contents)
        logging.debug(f"File {file_name} written to {path_to_save_to} on the disk.")

    def receive_file(self, client, path_to_save_to, file_name):   # Should be in the Comms Manager
        file_size = client.sock.recv(buffer_size).decode()
        logging.info("File size is:", file_size, "bytes")

        finished = False
        index = 0
        file_contents = b""

        while not finished:
            connection_confirmation = client.sock.recv(buffer_size)

            index += 1
            if index % 10 == 0:
                logging.debug("received data", index, "/", math.ceil(int(file_size) / buffer_size))

            if connection_confirmation.endswith(end_flag):
                finished = True
                file_contents += connection_confirmation[:-len(end_flag)]
            else:
                file_contents += connection_confirmation

        logging.info("finished receiving data")

        self.write_file_to_disk(file_contents, path_to_save_to, file_name)