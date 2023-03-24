from pydantic import BaseModel
from app.controllers.register import register_verification
from fastapi import Request
from app.models.responses import Response_tokens
from app.models.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/register'
)


@router.post('/')
async def register(user: User, request: Request):
    result = await register_verification(user, request)
    return result
