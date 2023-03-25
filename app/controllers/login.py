from app.utils.password import Crypt_password
from app.utils.token import Json_web_token
from app.database.users import db_users
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from app.models.user import User
from app.utils.check_input import check_email
from ..database.database import db


async def checking_email(email: str):
    if check_email(email) == False:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.INVALID_EMAIL_ADRESS.value)
    try:
        var = await db["users"].find_one({'email': email})
    except:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.CHECKING_USER.value)
    if var == None:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.EMAIL_ALREADY_EXIST.value)


def checking_password(password: str, hashed_password):
    crypt = Crypt_password(password)
    if (crypt.compare(hashed_password) != True):
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.BAD_PASSWORD.value)


def checking_username(username: str):
    if len(username) < 5:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.USERNAME_LENGTH.value)


def create_tokens(id: str):
    token = Json_web_token(id)
    access_token = token.encode_access_token()
    refresh_token = token.encode_refresh_token()
    return {
        'refresh_token': refresh_token,
        'access_token': access_token,
        'expires_in': "1800s",
        'token_type': "Bearer",
    }


async def login_verification(user: User):
    db = db_users()
    get_user = await db.get_user_with_email(user)
    checking_password(user.password, get_user['password'])
    await checking_email(user.email)
    return create_tokens(str(get_user['_id']))
