import logging


class UserService:
    def __init__(self):
        pass

    def create_user(self, username, password_hash):
        logging.info("Creating User", username, password_hash)
