from fastapi import APIRouter, Request

from app.controllers.create_my_week import my_week

router = APIRouter(
    prefix='/create_my_week'
)


@router.get('/')
async def create_my_week(request: Request):
    my_week_controller = my_week()
    authorization = request.headers.get('Authorization')
    result = await my_week_controller.create_my_week_verification(authorization)
    return result
