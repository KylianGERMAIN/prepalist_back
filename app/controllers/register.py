import os
from app.controllers.login import checking_email
from app.utils.check_input import check_email
from app.utils.password import Crypt_password
from app.utils.token import Json_web_token
from app.database.users import db_users
from app.utils.custom_error_message import Custom_Error_Message
from app.models.user import IUser
from ..database.database import db


async def checking_email(email: str):
    if check_email(email) == False:
        raise NameError(Custom_Error_Message.INVALID_EMAIL_ADRESS.value, 400)
    var = await db["users"].find_one({'email': email})
    if var != None:
        raise NameError(Custom_Error_Message.EMAIL_ALREADY_EXIST.value, 409)


def checking_password(password: str):
    if len(password) < 7:
        raise NameError(Custom_Error_Message.PASSWORD_LENGTH.value, 403)


def checking_username(username: str):
    if len(username) < 5:
        raise NameError(Custom_Error_Message.USERNAME_LENGTH.value, 403)


def create_tokens(id: str):
    token = Json_web_token(id)
    access_token = token.encode_token(os.getenv(
        'JWT_SECRET_ACCESS_TOKEN'), True)
    refresh_token = token.encode_token(os.getenv(
        'JWT_SECRET_REFRESH_TOKEN'), False)
    return {
        'refresh_token': refresh_token,
        'access_token': access_token,
        'expires_in': "1800s",
        'token_type': "Bearer",
    }


async def register_verification(user: IUser):
    db = db_users()
    checking_password(user.password)
    checking_username(user.username)
    await checking_email(user.email)
    crypt = Crypt_password(user.password)
    user.password = crypt.encrypt()
    created_user_id = await db.add_user(user)
    result = create_tokens(str(created_user_id))
    return (result)
