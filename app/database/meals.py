

from fastapi import HTTPException
from app.models.meal import Meal
from app.utils.custom_error_message import Custom_Error_Message
from ..database.database import db


class db_meals:
    async def add_meal(self, meal: Meal):
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
