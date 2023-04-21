
from fastapi import APIRouter, Request
from app.controllers.meal import meals

from app.models.meal import IMeal

router = APIRouter(
    prefix='/meal'
)


@router.post('/', response_model=IMeal, status_code=201)
async def add_meal(request: Request, meal: IMeal):
    meal_controller = meals()
    authorization = request.headers.get('Authorization')
    result = await meal_controller.create_meal(authorization, meal)
    return result


@router.put('/{id}')
async def update_meal(id, request: Request, meal: IMeal):
    meal_controller = meals()
    authorization = request.headers.get('Authorization')
    result = await meal_controller.update_meal(authorization, meal, id)
    return result


@router.delete('/{id}', status_code=202)
async def remove_meal(id, request: Request):
    meal_controller = meals()
    authorization = request.headers.get('Authorization')
    result = await meal_controller.delete_meal(authorization, id)
    return result
