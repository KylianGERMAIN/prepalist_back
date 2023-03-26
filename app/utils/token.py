import datetime
from fastapi import HTTPException
import jwt
import os

from app.utils.custom_error_message import Custom_Error_Message


class Json_web_token:
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def encode_token(self, env: str):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=52, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'id': self.__id
        }
        encoded_jwt = jwt.encode(
            payload, env, algorithm=os.getenv('JWT_ALGORITHM'))
        return encoded_jwt

    def decode_token(self, encoded_jwt: str, env: str):
        encoded_jwt = encoded_jwt.split()
        if (len(encoded_jwt) != 2):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.INVALID_TOKEN.value)
        elif (encoded_jwt[0] != 'Bearer'):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.INVALID_TOKEN.value)
        else:
            try:
                decode_jwt = jwt.decode(
                    encoded_jwt[1], env, algorithms=os.getenv('JWT_ALGORITHM'))
                return decode_jwt
            except:
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.INVALID_TOKEN.value)
