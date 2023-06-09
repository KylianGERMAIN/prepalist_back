import os
from app.utils.password import Crypt_password
from app.utils.token import Json_web_token
from app.database.users import db_users
from app.utils.custom_error_message import Custom_Error_Message
from app.models.user import IUser
from app.utils.check_input import check_email
from ..database.database import db


async def checking_email(email: str):
    if check_email(email) == False:
        raise NameError(
            Custom_Error_Message.INVALID_EMAIL_ADRESS.value, 400)
    var = await db["users"].find_one({'email': email})
    if var == None:
        raise NameError(
            Custom_Error_Message.USER_DOES_NOT_EXIST.value, 403)


def checking_password(password: str, hashed_password):
    crypt = Crypt_password(password)
    crypt.compare(hashed_password)


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


async def login_verification(user: IUser):
    db = db_users()
    get_user = await db.get_user_with_email(user)
    await checking_email(user.email)
    checking_password(user.password, get_user['password'])
    return create_tokens(str(get_user['_id']))
