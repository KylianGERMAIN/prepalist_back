from fastapi import APIRouter, HTTPException, Request
from app.controllers.week import week
from app.models.week import IWeek
from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/week'
)


@router.get('/generate')
async def generate_my_week(request: Request):
    try:
        my_week_controller = week()
        authorization = request.headers.get('Authorization')
        result = await my_week_controller.generate_my_week(authorization)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.WEEK_NOT_GENERATED.value)


@router.get('/')
async def get_my_week(request: Request):
    try:
        my_week_controller = week()
        authorization = request.headers.get('Authorization')
        result = await my_week_controller.get_my_week(authorization)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.WEEK_NOT_GENERATED.value)


@router.post('/')
async def create_my_week(request: Request, new_week: IWeek):
    try:
        my_week_controller = week()
        authorization = request.headers.get('Authorization')
        result = await my_week_controller.create_my_week_verification(authorization, new_week)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.WEEK_NOT_GENERATED.value)
