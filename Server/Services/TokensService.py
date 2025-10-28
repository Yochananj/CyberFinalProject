import jwt
import time



class TokensService:
    def __init__(self, private_key, public_key):
        self.private_key = private_key
        self.public_key = public_key

    def create_token(self, user_id):
        return jwt.encode({"user_id": user_id, "exp": int(time.time() + 10*60)}, self.private_key, algorithm="RS256") # 10 minutes

    def is_token_valid(self, token):
        decoded_token = self.decode_token(token)
        if decoded_token["exp"] > int(time.time()):
            return True
        else:
            return False

    def does_token_need_refreshing(self, token):
        decoded_token = self.decode_token(token)
        if decoded_token["exp"] - 2*60 > int(time.time()): # 2 minutes
            return True
        else:
            return False

    def decode_token(self, token):
        return jwt.decode(token, self.public_key, algorithms=["RS256"])