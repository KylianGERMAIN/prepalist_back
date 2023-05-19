import datetime
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

    def encode_token(self, env: str, access: bool):

        if access == True:
            time = datetime.timedelta(minutes=30, seconds=0)
        else:
            time = datetime.timedelta(weeks=52, seconds=0)

        payload = {
            'exp': datetime.datetime.utcnow() + time,
            'iat': datetime.datetime.utcnow(),
            'id': self.__id
        }
        encoded_jwt = jwt.encode(
            payload, env, algorithm=os.getenv('JWT_ALGORITHM'))
        return encoded_jwt

    def decode_token(self, encoded_jwt: str, env: str):
        encoded_jwt = encoded_jwt.split()
        if (len(encoded_jwt) != 2):
            raise NameError(Custom_Error_Message.INVALID_TOKEN.value, 403)
        elif (encoded_jwt[0] != 'Bearer'):
            raise NameError(Custom_Error_Message.INVALID_TOKEN.value, 403)
        else:
            decode_jwt = jwt.decode(
                encoded_jwt[1], env, algorithms=os.getenv('JWT_ALGORITHM'))
            return decode_jwt

    def checking_authorization(self, authorization: str):
        try:
            if (authorization == None):
                raise NameError(
                    Custom_Error_Message.NO_AUTHORIZATION.value, 403)
            payload = self.decode_token(authorization, os.getenv(
                'JWT_SECRET_ACCESS_TOKEN'))
            self.set_id(payload['id'])
        except:
            raise NameError(Custom_Error_Message.INVALID_TOKEN.value, 403)

    def checking_authorization_refresh(self, authorization: str):
        if (authorization == None):
            raise NameError(Custom_Error_Message.NO_AUTHORIZATION.value, 401)
        payload = self.decode_token(authorization, os.getenv(
            'JWT_SECRET_REFRESH_TOKEN'))
        self.set_id(payload['id'])
