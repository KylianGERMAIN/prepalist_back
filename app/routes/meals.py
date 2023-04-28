
from fastapi import APIRouter, Request
from app.controllers.meal import meals

from app.models.meal import IMeal

router = APIRouter(
    prefix='/meals'
)


@router.get('/', status_code=200)
async def get_meal(request: Request):
    meal_controller = meals()
    authorization = request.headers.get('Authorization')
    result = await meal_controller.get_meals(authorization)
    return result
