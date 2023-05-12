
import os
from fastapi import APIRouter, Request
from app.controllers.meal import meals

from app.models.meal import IMeal
from app.utils.token import Json_web_token

router = APIRouter(
    prefix='/refresh_token'
)


@router.get('/', status_code=200)
async def refresh_token(request: Request):
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
