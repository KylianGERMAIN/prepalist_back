from app.models.user import IUser
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


class db_users:

    async def add_user(self, user: IUser):
        try:
            request = await db["users"].insert_one(
                {'username': user.username, 'email': user.email, 'password': str(user.password)})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.ADD_USER.value)

    async def get_user_with_email(self, user: IUser):
        try:
            request = await db["users"].find_one(
                {'email': user.email})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.CHECKING_USER.value)
