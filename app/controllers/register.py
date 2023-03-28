import os
from app.utils.password import Crypt_password
from app.utils.token import Json_web_token
from app.database.users import db_users
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from app.models.user import IUser
from app.utils.check_input import check_email
from ..database.database import db


async def checking_email(email: str):
    if check_email(email) == False:
        raise HTTPException(
            status_code=400, detail=Custom_Error_Message.INVALID_EMAIL_ADRESS.value)
    try:
        var = await db["users"].find_one({'email': email})
    except:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.CHECKING_USER.value)
    if var != None:
        raise HTTPException(
            status_code=409, detail=Custom_Error_Message.EMAIL_ALREADY_EXIST.value)


def checking_password(password: str):
    if len(password) < 7:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.PASSWORD_LENGTH.value)


def checking_username(username: str):
    if len(username) < 5:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.USERNAME_LENGTH.value)


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
    created_user = await db.add_user(user)
    result = create_tokens(str(created_user))
    return (result)
