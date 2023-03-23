from app.models.user import User
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import Request, HTTPException


class db_users:
    def __init__(self, request: Request):
        self.__request = request

    def add_user(self, user: User):
        try:
            request = self.__request.app.database["users"].insert_one(
                {'username': user.username, 'email': user.email, 'password': str(user.password), })
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.ADD_USER.value)
