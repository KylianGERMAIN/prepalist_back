from app.controllers.register import register_verification
from app.models.responses import Response_tokens
from app.models.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/register'
)


@router.post('/', response_model=Response_tokens)
async def register(user: User):
    result = await register_verification(user)
    return result
