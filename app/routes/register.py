from app.controllers.password import Crypt_password
from app.controllers.register import register_verification
from fastapi import Request
from app.models.user import User

from fastapi import APIRouter

router = APIRouter(
    prefix='/register'
)


@router.post('/')
def register(user: User, request: Request):
    return register_verification(user, request)
