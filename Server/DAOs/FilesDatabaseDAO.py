import logging
import peewee
import os
from Dependencies.Constants import server_storage_path

db_path = os.path.join(server_storage_path, "Files.db")
files_db = peewee.SqliteDatabase(db_path)

class FilesDB(peewee.Model):
    file_id = peewee.AutoField()
    file_owner_id = peewee.IntegerField()
    user_file_path = peewee.CharField()
    file_uuid = peewee.CharField()
    user_file_name = peewee.CharField()
    file_size = peewee.IntegerField()

    class Meta:
        database = files_db
        indexes = (
        (("file_owner_id", "user_file_path", "user_file_name"), True),)


class FilesDatabaseDAO:
    def __init__(self):
        files_db.connect()
        logging.debug(f"Connected to the Database at {db_path}.")
        files_db.create_tables([FilesDB])

    def create_file(self, file_owner_id, user_file_path, file_uuid,  user_file_name, file_size):
        FilesDB.create(file_owner_id=file_owner_id, user_file_path=user_file_path, file_uuid=file_uuid, user_file_name=user_file_name, file_size=file_size)
        logging.debug(f"File {user_file_name} created in {file_owner_id}/{user_file_path} in the Database.")

    def delete_file(self, file_owner_id, user_file_path, user_file_name):
        FilesDB.delete().where(FilesDB.user_file_name == user_file_name and FilesDB.file_owner_id == file_owner_id and FilesDB.user_file_path == user_file_path).execute()
        logging.debug(f"File {user_file_name} deleted from {file_owner_id}/{user_file_path} in the Database.")

    def get_file_size(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(FilesDB.file_owner_id == file_owner_id and FilesDB.user_file_path == user_file_path and FilesDB.user_file_name == user_file_name).get().file_size

    def get_file_uuid(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(FilesDB.file_owner_id == file_owner_id and FilesDB.user_file_path == user_file_path and FilesDB.user_file_name == user_file_name).get().file_uuid

    def does_file_exist(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(FilesDB.file_owner_id == file_owner_id and FilesDB.user_file_path == user_file_path and FilesDB.user_file_name == user_file_name).exists()

    def close_db(self):
        files_db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    dao = FilesDatabaseDAO()
    dao.create_file(123,  "/a/b/c/d/", 123123, "bloop.txt", 12345)
    files_db.close()