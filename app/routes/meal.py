
from fastapi import APIRouter, Request
from app.controllers.meal import create_meal

from app.models.meal import Meal

router = APIRouter(
    prefix='/meal'
)


@router.post('/')
async def meal(request: Request, meal: Meal):
    authorization = request.headers.get('Authorization')
    await create_meal(authorization, meal)
    return {'meal': 'meal'}
