import datetime
import jwt
import os


class Json_web_token:
    def __init__(self, id):
        self.__id = id

    def encode_access_token(self):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'id': self.__id
        }
        encoded_jwt = jwt.encode(payload, os.getenv(
            'JWT_SECRET_ACCESS_TOKEN'), algorithm=os.getenv('JWT_ALGORITHM'))
        return encoded_jwt

    def encode_refresh_token(self):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=52, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'id': self.__id
        }
        encoded_jwt = jwt.encode(payload, os.getenv(
            'JWT_SECRET_REFRESH_TOKEN'), algorithm=os.getenv('JWT_ALGORITHM'))
        return encoded_jwt

    def decode_access_token(self, encoded_jwt):
        decode_jwt = jwt.decode(encoded_jwt, os.getenv(
            'JWT_SECRET_ACCESS_TOKEN'), algorithms=os.getenv('JWT_ALGORITHM'))
        return decode_jwt

    def decode_refresh_token(self, encoded_jwt):
        decode_jwt = jwt.decode(encoded_jwt, os.getenv(
            'JWT_SECRET_REFRESH_TOKEN'), algorithms=os.getenv('JWT_ALGORITHM'))
        return decode_jwt
