import uuid
import logging
from Server.DAOs import FilesDatabaseDAO
from Server.DAOs.FilesDiskDAO import FilesDiskDAO
from Server.Services.UsersService import UsersService


class FileService:
    def __init__(self):
        self.files_database_dao = FilesDatabaseDAO.FilesDatabaseDAO()
        self.files_disk_dao = FilesDiskDAO()
        self.users_service = UsersService()

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
        else:
            logging.error("File already exists.")

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

    def file_uuid_generator(self):
        return uuid.uuid4().hex





if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    file_service = FileService()
    temp_username = str(file_service.file_uuid_generator())
    temp_filename = str(file_service.file_uuid_generator())
    file_service.users_service.create_user(temp_username, "123456789")
    file_service.create_file(temp_username, "/a/b/c/d/", temp_filename, b"hello world")
    print(file_service.get_file_contents(temp_username,  "/a/b/c/d/", temp_filename))
    file_service.delete_file(temp_username, "/a/b/c/d/", temp_filename)



