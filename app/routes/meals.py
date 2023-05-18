
from fastapi import APIRouter, HTTPException, Request
from app.controllers.meal import meals

from app.models.meal import IMeal
from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/meals'
)


@router.get('/', status_code=200)
async def get_meal(request: Request):
    try:
        meal_controller = meals()
        authorization = request.headers.get('Authorization')
        result = await meal_controller.get_meals(authorization)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.FIND_MEALS.value)
