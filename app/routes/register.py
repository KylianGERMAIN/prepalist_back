from app.controllers.register import register_verification
from app.models.responses import Response_tokens
from app.models.user import IUser
from fastapi import APIRouter

router = APIRouter(
    prefix='/register'
)


@router.post('/', response_model=Response_tokens, status_code=401)
async def register(user: IUser):
    result = await register_verification(user)
    return result
