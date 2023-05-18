from app.controllers.register import register_verification
from app.models.responses import Response_tokens
from app.models.user import IUser
from fastapi import APIRouter, HTTPException

from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/register'
)


@router.post('/', response_model=Response_tokens, status_code=201)
async def register(user: IUser):
    try:
        result = await register_verification(user)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.REGISTER_USER.value)
