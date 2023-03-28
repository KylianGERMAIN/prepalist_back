

from bson import ObjectId
from fastapi import HTTPException
from app.models.meal import IMeal
from app.utils.custom_error_message import Custom_Error_Message
from ..database.database import db


class db_meals:
    async def add_meal(self, meal: IMeal):
        try:
            ingredient_list = []
            for i in meal.ingredients:
                ingredient_list.append({'ingredient': i.ingredient})
            request = await db["meals"].insert_one(
                {'name': meal.name, 'ingredients': ingredient_list})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.ADD_USER.value)

    async def remove_meal(self, id: str):
        try:
            request = await db["meals"].delete_one(
                {'_id': ObjectId(id)})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.REMOVE_MEAL.value)

    async def find_meal(self, id: str):
        try:
            request = await db["meals"].find_one(
                {'_id': ObjectId(id)})
            if request == None:
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.MEAL_DOES_NOT_EXIST.value)
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.FIND_MEAL.value)
