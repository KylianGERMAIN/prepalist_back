from app.controllers.login import login_verification
from app.models.responses import Response_tokens
from app.models.user import IUser
from fastapi import APIRouter, HTTPException

from app.utils.custom_error_message import Custom_Error_Message

router = APIRouter(
    prefix='/login'
)


@router.post('/', response_model=Response_tokens)
async def login(user: IUser):
    try:
        result = await login_verification(user)
        return result
    except NameError as e:
        raise HTTPException(
            status_code=e.args[1], detail=e.args[0])
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.LOGIN_USER.value)
