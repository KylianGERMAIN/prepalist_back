from app.models.user import IUser
from app.utils.custom_error_message import Custom_Error_Message
from ..database.database import db


class db_users:

    async def add_user(self, user: IUser):
        request = await db["users"].insert_one(
            {'username': user.username, 'email': user.email, 'password': str(user.password)})
        return request.inserted_id

    async def get_user_with_email(self, user: IUser):
        request = await db["users"].find_one(
            {'email': user.email})
        return request
