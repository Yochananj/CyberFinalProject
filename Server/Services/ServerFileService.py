import logging
import uuid

from Server.DAOs import FilesDatabaseDAO
from Server.DAOs.FilesDiskDAO import FilesDiskDAO
from Server.Services.UsersService import UsersService


class FileService:
    def __init__(self, users_service: UsersService):
        self.files_database_dao = FilesDatabaseDAO.FilesDatabaseDAO()
        self.files_disk_dao = FilesDiskDAO()
        self.users_service = users_service

    def create_file(self, file_owner, user_file_path, user_file_name, file_contents):
        file_owner_id = self.users_service.get_user_id(file_owner)
        if not self.files_database_dao.does_file_exist(file_owner_id, user_file_path, user_file_name):
            # write to disk
            file_uuid = self.file_uuid_generator()
            self.files_disk_dao.write_file_to_disk(file_owner_id, file_uuid, file_contents)

            # create in database
            file_size = self.files_disk_dao.get_file_size_on_disk(file_owner_id, file_uuid)
            self.files_database_dao.create_file(file_owner_id, user_file_path, file_uuid, user_file_name, file_size)

            logging.debug(f"File {user_file_name} created.")
            return True
        else:
            logging.error("File already exists.")
            return False

    def delete_file(self, file_owner, user_file_path, user_file_name):
        file_owner_id = self.users_service.get_user_id(file_owner)
        file_uuid = self.files_database_dao.get_file_uuid(file_owner_id, user_file_path, user_file_name)
        if self.files_database_dao.does_file_exist(file_owner_id, user_file_path, user_file_name):
            # delete from disk
            self.files_disk_dao.delete_file_from_disk(file_owner_id, file_uuid)

            # delete from database
            self.files_database_dao.delete_file(file_owner_id, user_file_path, user_file_name)
            logging.debug(f"File {user_file_name} deleted.")
        else:
            logging.error("File does not exist.")

    def get_file_contents(self, file_owner, user_file_path, file_name):
        file_owner_id = self.users_service.get_user_id(file_owner)
        file_uuid = self.files_database_dao.get_file_uuid(file_owner_id, user_file_path, file_name)
        file_contents = self.files_disk_dao.get_file_contents(file_owner_id, file_uuid)
        return file_contents

    def get_file_size(self, file_owner, user_file_path, file_name):
        return self.files_database_dao.get_file_size(file_owner, user_file_path, file_name)

    def get_dirs_list_for_path(self, file_owner, path):
        logging.debug(f"Getting dirs list for path {path} for user {file_owner}.")
        file_owner_id = self.users_service.get_user_id(file_owner)

        dirs_in_path = self.files_database_dao.get_all_dirs_in_path(file_owner_id, path)

        directories_list = []
        for directory in dirs_in_path:
            temp_dir = Directory(directory.user_file_path, len(self.files_database_dao.get_all_files_in_path(file_owner_id, directory.user_file_path)))
            if temp_dir.path not in [a.path for a in directories_list]:
                directories_list.append(temp_dir)
        logging.debug(f"Filtered dirs list: {directories_list}")
        return directories_list

    def get_files_list_in_path(self, file_owner, path):
        logging.debug(f"Getting files list for path {path} for user {file_owner}.")
        file_owner_id = self.users_service.get_user_id(file_owner)
        files = self.files_database_dao.get_all_files_in_path(file_owner_id, path)
        files_list = []
        for file in files:
            files_list.append(File(file.user_file_name, file.file_size))
        logging.debug(f"File tuples list: {[file.__dict__ for file in files_list]}")
        return files_list

    def file_uuid_generator(self):
        return uuid.uuid4().hex

    def can_create_file(self, file_owner, user_file_path, user_file_name):
        file_owner_id = self.users_service.get_user_id(file_owner)
        if self.files_database_dao.does_file_exist(file_owner_id, user_file_path, user_file_name):
            return False
        else:
            return True

class Directory:
    def __init__(self, path, item_count):
        self.path = path
        self.item_count = item_count

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    file_service = FileService()
    temp_username = str(file_service.file_uuid_generator())
    temp_filename = str(file_service.file_uuid_generator())
    file_service.users_service.create_user(temp_username, "123456789")
    file_service.create_file(temp_username, "/a/b/c/d/", temp_filename, b"hello world")
    print(file_service.get_file_contents(temp_username,  "/a/b/c/d/", temp_filename))
    file_service.delete_file(temp_username, "/a/b/c/d/", temp_filename)



