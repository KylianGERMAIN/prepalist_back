from app.controllers.list import list_ingredients
from app.controllers.login import login_verification
from app.models.responses import Response_tokens
from app.models.user import IUser
from fastapi import APIRouter, Request

router = APIRouter(
    prefix='/list'
)


@router.get('/')
async def get_list(request: Request):
    list_controller = list_ingredients()
    authorization = request.headers.get('Authorization')
    result = await list_controller.get_list(authorization)
    return result
