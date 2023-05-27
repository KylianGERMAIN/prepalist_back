from app.controllers.list import list_ingredients
from fastapi import APIRouter, HTTPException, Request

from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/list'
)


@router.get('/')
async def get_list(request: Request):
    try:
        list_controller = list_ingredients()
        authorization = request.headers.get('Authorization')
        result = await list_controller.get_list(authorization)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.CHECKING_LIST_INGREDIENTS.value)
