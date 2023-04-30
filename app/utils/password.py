import bcrypt
from fastapi import HTTPException

from app.utils.custom_error_message import Custom_Error_Message


class Crypt_password:
    def __init__(self, password):
        self.__password = password

    def encrypt(self):
        password = self.__password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password

    def compare(self, hashed_password):
        if bcrypt.hashpw(self.__password, hashed_password) == hashed_password:
            return True
        else:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.BAD_PASSWORD.value)
