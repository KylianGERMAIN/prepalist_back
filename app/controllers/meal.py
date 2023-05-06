import os

from bson import ObjectId
from app.database.meals import db_meals
from app.models.meal import IMeal
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException
from ..database.database import db


class meals:

    async def checking_meal(self, meal: IMeal, token: Json_web_token):
        if (meal.name == None or meal.name == ''):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.MEAL_NO_NAME.value)
        try:
            var = await db["meals"].find_one({'name': meal.name, 'user_id': ObjectId(token.get_id())})
        except:
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.CHECKING_MEAL.value)
        if var != None:
            raise HTTPException(
                status_code=409, detail=Custom_Error_Message.MEAL_ALREADY_EXIST.value)
        if (len(meal.ingredients) <= 0):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.NO_INGREDIENTS.value)

    async def create_meal(self, authorization: str, meal: IMeal):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        await self.checking_meal(meal, token)
        result = await db.add_meal(meal, token)
        meal.id = str(result.inserted_id)
        return meal

    async def update_meal(self, authorization: str, meal: IMeal, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        meal.id = id
        await db.find_meal(id, token)
        await db.update_meal(id, token, meal)
        response = await db.find_meal(id, token)
        return {
            'id': str(response['_id']),
            'name': response['name'],
            'ingredients': response['ingredients'],
            'created_at': response['created_at']
        }

    async def delete_meal(self, authorization: str, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        await db.find_meal(id, token)
        await db.remove_meal(id, token)
        return {'message': 'Meal deleted'}

    async def get_meal(self, authorization: str, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        response = await db.find_meal(id, token)
        return {
            'id': str(response['_id']),
            'name': response['name'],
            'ingredients': response['ingredients'],
            'created_at': response['created_at']
        }

    async def get_meals(self, authorization: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        response = await db.find_meals(token)
        return response
