import os

from bson import ObjectId
from app.database.meals import db_meals
from app.models.meal import IMeal
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


class list_ingredients:

    async def get_list(self, authorization: str):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        # request = await db["weeks"].find_one(
        #     {'user_id': ObjectId(token.get_id())})
        # for value in request['date']:
        #     print('__________________________')
        #     print(value)
        #     print(value['lunch']['name'])

        # for (key, value) in request.items():
        #     print(key, value)
        return {'message': 'eazeaz'}
