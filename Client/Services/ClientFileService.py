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


    def read_file_from_disk(self, full_file_path):
        with open(full_file_path, "rb") as file:
            file_contents = file.read(-1)
        return file_contents