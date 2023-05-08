import itertools
from bson import ObjectId
from app.database.meals import db_meals
from app.models.meal import IMeal
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


class list_ingredients:

    async def get_list(self, authorization: str):
        try:
            token = Json_web_token('no id')
            token.checking_authorization(authorization)
            request = await db["weeks"].find_one(
                {'user_id': ObjectId(token.get_id())})
            list_meal_id = list()
            list_ingredients = list()
            for value in request['date']:
                list_meal_id.append(ObjectId(value['dinner']['id']))
            print(len(list_meal_id))
            if (len(list_meal_id) != 7):
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.NO_ENOUGH_MEAL_TO_GET_INGREDIENTS.value)
            else:
                async for doc in db["meals"].find({'user_id': ObjectId(
                    token.get_id()), "_id": {
                    "$in":
                    list_meal_id
                }}):
                    list_ingredients.append(doc['ingredients'])
                return {'ingredients': list(itertools.chain.from_iterable(list_ingredients))}
        except:
            if (len(list_meal_id) != 7):
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.NO_ENOUGH_MEAL_TO_GET_INGREDIENTS.value)
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.CHECKING_LIST_INGREDIENTS.value)
