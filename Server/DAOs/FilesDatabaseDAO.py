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
        FilesDB.delete().where(
            (FilesDB.user_file_name == user_file_name),
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path == user_file_path)
        ).execute()
        logging.debug(f"File {user_file_name} deleted from {file_owner_id}/{user_file_path} in the Database.")

    def get_file_size(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path == user_file_path),
            (FilesDB.user_file_name == user_file_name)
        ).get().file_size


    def get_file_uuid(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path == user_file_path),
            (FilesDB.user_file_name == user_file_name)
        ).get().file_uuid

    def does_file_exist(self, file_owner_id, user_file_path, user_file_name):
        return FilesDB.select().where(
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path == user_file_path),
            (FilesDB.user_file_name == user_file_name)
        ).exists()

    def get_all_files_in_path(self, file_owner_id, path):
        return FilesDB.select().where(
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path == path)
        )

    def get_all_dirs_in_path(self, file_owner_id, path):
        lst = list(
            FilesDB.select().where(
                (FilesDB.file_owner_id == file_owner_id),
                (FilesDB.user_file_path.startswith(path))
            )
        )
        logging.debug(f"Dirs that start with: {lst} \n Filtering...")
        lst = self._truncate_dirs_to_one_deeper(lst, path)
        return lst

    def get_number_of_dirs_in_dir(self, file_owner_id, dir_path):
        lst = FilesDB.select().where(
            (FilesDB.file_owner_id == file_owner_id),
            (FilesDB.user_file_path.startswith(dir_path)),
            (len(dir_path.split("/")) == len(str(FilesDB.user_file_path).split("/")) + 1)
        )
        lst = [item.user_file_path for item in lst]
        filtered = []
        for item in lst:
            if item not in filtered:
                filtered.append(item)
        return len(filtered)



    def _truncate_dirs_to_one_deeper(self, lst: list, path):
        logging.debug(f"Truncating dirs not one dir deeper than {path} to one deeper.")
        required_dirs_deep = len(self._filter_empty_strings(path.split("/"))) + 1
        logging.debug(f"Required Dirs Deep: {required_dirs_deep}")

        to_return_list = []

        for item in lst:
            logging.debug(f"Checking {item.user_file_path}")
            file_path_parts = self._filter_empty_strings(str(item.user_file_path).split("/"))
            if len(file_path_parts) == required_dirs_deep:
                logging.debug(f"Item {item.user_file_path} is one dir deeper than path.")
                to_return_list.append(item)
            elif len(file_path_parts) > required_dirs_deep:
                logging.debug(f"Item {item.user_file_path} is more than one dir deeper than path. \n Refactoring...")
                refactored_path = "/"
                for i in range(required_dirs_deep - 1):
                    refactored_path += file_path_parts[i] + "/"
                refactored_path += file_path_parts[required_dirs_deep - 1]
                logging.debug(f"Refactored Path: {refactored_path}")
                item.user_file_path = refactored_path
                to_return_list.append(item)
            else:
                logging.debug(f"Item {item.user_file_path} is not one dir deeper than path. \n Skipping...")

        return to_return_list

    def _filter_empty_strings(self, list_to_filter: list):
        logging.debug(f"Filtering empty strings from list {list_to_filter}.")
        to_return_list = []
        for item in list_to_filter:
            if len(item) != 0:
                to_return_list.append(item)
        logging.debug(f"Filtered list: {to_return_list}")
        return to_return_list

    def close_db(self):
        files_db.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    dao = FilesDatabaseDAO()
    for file in dao.get_all_dirs_in_path(123, '/a'):
        print(file.user_file_path)
    files_db.close()