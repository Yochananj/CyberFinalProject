import logging
import peewee

files_db = peewee.SqliteDatabase("Files.db")

class FilesDB(peewee.Model):
    file_id = peewee.AutoField()
    file_name = peewee.CharField()
    file_owner = peewee.CharField()
    file_size = peewee.IntegerField()
    file_path = peewee.CharField()
    file_contents = peewee.BlobField()

    class Meta:
        database = files_db
        indexes = (
        (("file_name", "file_owner", "file_path"), True),
        )


class FilesDAO:
    def create_file(self, file_name, file_owner, file_size, file_path, file_contents):
        if not (FilesDB.select().where(FilesDB.file_path == file_path)).select().where(FilesDB.file_name == file_name and FilesDB.file_owner == file_owner).exists():
            FilesDB.create(file_name=file_name, file_owner=file_owner, file_size=file_size, file_path=file_path,
                           file_contents=file_contents)
            logging.debug(f"File {file_name} (Owner: {file_owner}) created in {file_path}.")
        else:
            logging.error("File already exists.")

    def get_file_property(self, file_property, file_name, file_owner, file_path):
        match file_property:
            case "file_size":
                return FilesDB.select().where(FilesDB.file_name == file_name and FilesDB.file_owner == file_owner and FilesDB.file_path == file_path).get().file_size
            case "file_contents":
                return FilesDB.select().where(FilesDB.file_name == file_name and FilesDB.file_owner == file_owner and FilesDB.file_path == file_path).get().file_contents
            case _:
                logging.error("Invalid property.")
                return None

    def delete_file(self, file_name, file_owner, file_path):
        FilesDB.delete().where(FilesDB.file_name == file_name and FilesDB.file_owner == file_owner and FilesDB.file_path == file_path).execute()
        logging.debug(f"File {file_name} (Owner: {file_owner}) deleted from {file_path}.")




if __name__ == "__main__":
    files_db.connect()
    files_db.create_tables([FilesDB])
    files_db.close()