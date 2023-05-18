
from fastapi import APIRouter, HTTPException, Request
from app.controllers.meal import meals

from app.models.meal import IMeal
from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/meal'
)


@router.post('/', response_model=IMeal, status_code=201)
async def add_meal(request: Request, meal: IMeal):
    try:
        meal_controller = meals()
        authorization = request.headers.get('Authorization')
        result = await meal_controller.create_meal(authorization, meal)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.ADD_MEAL.value)


@router.get('/{id}', response_model=IMeal, status_code=200)
async def get_meal(id, request: Request):
    try:
        meal_controller = meals()
        authorization = request.headers.get('Authorization')
        result = await meal_controller.get_meal(authorization, id)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.FIND_MEAL.value)


@router.put('/{id}')
async def update_meal(id, request: Request, meal: IMeal):
    try:
        meal_controller = meals()
        authorization = request.headers.get('Authorization')
        result = await meal_controller.update_meal(authorization, meal, id)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.UPDATE_MEAL.value)


@router.delete('/{id}', status_code=202)
async def remove_meal(id, request: Request):
    try:
        meal_controller = meals()
        authorization = request.headers.get('Authorization')
        result = await meal_controller.delete_meal(authorization, id)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.REMOVE_MEAL.value)
