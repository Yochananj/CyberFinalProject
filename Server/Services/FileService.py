from Dependencies.Constants import *
import os
import logging
from Server.DAOs import FilesDAO


class FileService:
    def __init__(self):
        self.files_dao = FilesDAO.FilesDAO()

    def get_file(self, file_name, file_owner, file_path):
        file_size = self.files_dao.get_file_property("file_size", file_name, file_owner, file_path)
        file_contents = self.files_dao.get_file_property("file_contents", file_name, file_owner, file_path)
        return file_size, file_contents

    def create_file(self, file_name, file_owner, file_size, file_path, file_contents):
        self.files_dao.create_file(file_name, file_owner, file_size, file_path, file_contents)
        logging.debug("File created.")





    def send_file(self, client, path):                      # to be deprecated
        file_size = os.path.getsize(path)
        client.send(str(file_size).encode())
        with open(path, "rb") as file:
            contents = file.read(-1)
            client.sendall(contents)
            client.send(end_flag)

