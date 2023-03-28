from app.controllers.login import login_verification
from app.models.responses import Response_tokens
from app.models.user import IUser
from fastapi import APIRouter

router = APIRouter(
    prefix='/login'
)


@router.post('/', response_model=Response_tokens)
async def login(user: IUser):
    result = await login_verification(user)
    return result
