from fastapi import APIRouter

from app.controllers.create_my_week import create_my_week_verification

router = APIRouter(
    prefix='/create_my_week'
)


@router.get('/')
async def create_my_week():
    result = await create_my_week_verification()
    return result
