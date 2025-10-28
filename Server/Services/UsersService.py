import logging

from Server.DAOs.UsersDatabaseDAO import UsersDatabaseDAO


class UsersService:
    def __init__(self):
        self.users_database_dao = UsersDatabaseDAO()

    def create_user(self, username, password_hash):
        self.users_database_dao.create_user(username, password_hash)
        logging.debug(f"User {username} created.")

    def delete_user(self, username):
        self.users_database_dao.delete_user(username)
        logging.debug(f"User {username} deleted.")

    def get_user_id(self, username):
        return self.users_database_dao.get_user_id(username)
