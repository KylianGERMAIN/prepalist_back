import os
from app.models.meal import Meal
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


async def checking_authorization(authorization: str, token: Json_web_token):
    if (authorization == None):
        raise HTTPException(
            status_code=401, detail=Custom_Error_Message.NO_AUTHORIZATION.value)
    payload = token.decode_token(authorization, os.getenv(
        'JWT_SECRET_ACCESS_TOKEN'))
    token.set_id(payload['id'])


async def checking_meal(meal_name: str):
    try:
        var = await db["meals"].find_one({'name': meal_name})
    except:
        raise HTTPException(
            status_code=403, detail=Custom_Error_Message.CHECKING_MEAL.value)
    if var != None:
        raise HTTPException(
            status_code=409, detail=Custom_Error_Message.MEAL_ALREADY_EXIST.value)


async def create_meal(authorization: str, meal: Meal):
    token = Json_web_token('no id')
    await checking_authorization(authorization, token)
    await checking_meal(meal.name)
    print(authorization)
    print(meal.name)
    return {}
