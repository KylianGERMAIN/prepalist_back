

from bson import ObjectId
from fastapi import HTTPException
from app.models.meal import IMeal
from app.utils.custom_error_message import Custom_Error_Message
from app.utils.token import Json_web_token
from ..database.database import db


class db_meals:
    async def add_meal(self, meal: IMeal, token: Json_web_token):
        try:
            ingredient_list = []
            for i in meal.ingredients:
                ingredient_list.append({'ingredient': i.ingredient})
            request = await db["meals"].insert_one(
                {'user_id': ObjectId(token.get_id()), 'name': meal.name, 'ingredients': ingredient_list})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.ADD_USER.value)

    async def remove_meal(self, id: str, token: Json_web_token):
        try:
            request = await db["meals"].delete_one(
                {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())})
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.REMOVE_MEAL.value)

    async def find_meal(self, id: str, token: Json_web_token):
        try:
            request = await db["meals"].find_one(
                {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())})
            if request == None:
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.MEAL_DOES_NOT_EXIST.value)
            return request
        except:
            if request == None:
                raise HTTPException(
                    status_code=403, detail=Custom_Error_Message.MEAL_DOES_NOT_EXIST.value)
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.FIND_MEAL.value)

    async def update_meal(self, id: str, token: Json_web_token, meal: IMeal):
        try:
            filter = {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())}
            ingredient_list = []
            for i in meal.ingredients:
                ingredient_list.append({'ingredient': i.ingredient})
            new_values = {"$set": {'name': str(meal.name), 'ingredients':
                                   ingredient_list}}
            request = await db["meals"].update_one(filter, new_values)
            return request
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.UPDATE_MEAL.value)
