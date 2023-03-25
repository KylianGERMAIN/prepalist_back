from app.models.user import User
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


class db_users:

    async def add_user(self, user: User):
        try:
            request = await db["users"].insert_one(
                {'username': user.username, 'email': user.email, 'password': str(user.password)})
            print(request)
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.ADD_USER.value)
