from app.controllers.password import Crypt_password
from app.controllers.token import Json_web_token
from app.database.users import db_users
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException, Request
from app.models.user import User
from app.utils.check_input import check_email


def checking_email(email: str, request: Request):
    var = request.app.database["users"].find({'email': email})
    if len(list(var)) > 0:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.EMAIL_ALREADY_EXIST.value)
    if check_email(email) == False:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.INVALID_EMAIL_ADRESS.value)


def checking_password(password: str):
    if len(password) < 7:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.PASSWORD_LENGTH.value)


def checking_username(username: str):
    if len(username) < 5:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.USERNAME_LENGTH.value)


def create_tokens(id: str):
    print(id)
    token = Json_web_token(id)
    print(token)
    access_token = token.encode_access_token()
    refresh_token = token.encode_refresh_token()
    return {
        'refresh_token': refresh_token,
        'access_token': access_token,
        'expires_in': "1800s",
        'token_type': "Bearer",
    }


def register_verification(user: User, request: Request):
    db = db_users(request)
    checking_email(user.email, request)
    checking_password(user.password)
    checking_username(user.username)
    crypt = Crypt_password(user.password)
    user.password = crypt.encrypt()
    created_user = db.add_user(user)
    result = create_tokens(str(created_user.inserted_id))
    return (result)
