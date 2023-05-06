from fastapi import APIRouter, Request

from app.controllers.week import week

router = APIRouter(
    prefix='/week'
)


@router.get('/')
async def get_my_week(request: Request):
    my_week_controller = week()
    authorization = request.headers.get('Authorization')
    result = await my_week_controller.get_my_week(authorization)
    return result


@router.post('/')
async def create_my_week(request: Request):
    my_week_controller = week()
    authorization = request.headers.get('Authorization')
    result = await my_week_controller.create_my_week_verification(authorization)
    return result
