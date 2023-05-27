import os
from fastapi import APIRouter, HTTPException, Request
from app.utils.custom_error_message import Custom_Error_Message
from app.utils.token import Json_web_token

router = APIRouter(
    prefix='/refresh_token'
)


@router.get('/', status_code=200)
async def refresh_token(request: Request):
    try:
        authorization = request.headers.get('Authorization')
        token = Json_web_token('no id')
        token.checking_authorization_refresh(authorization)
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
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.GENERATION_REFRESH_TOKEN.value)
