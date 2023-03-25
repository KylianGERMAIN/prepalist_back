from app.controllers.login import login_verification
from app.models.responses import Response_tokens
from app.models.user import User
from fastapi import APIRouter

router = APIRouter(
    prefix='/login'
)


@router.post('/', response_model=Response_tokens)
async def login(user: User):
    result = await login_verification(user)
    return result
