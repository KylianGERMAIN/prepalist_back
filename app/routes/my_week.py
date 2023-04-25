from fastapi import APIRouter, Request

from app.controllers.create_my_week import my_week

router = APIRouter(
    prefix='/my_week'
)


@router.get('/')
async def get_my_week(request: Request):
    my_week_controller = my_week()
    authorization = request.headers.get('Authorization')
    result = await my_week_controller.get_my_week(authorization)
    return result
