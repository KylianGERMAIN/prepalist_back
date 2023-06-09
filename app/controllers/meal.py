from bson import ObjectId
from app.database.meals import db_meals
from app.models.meal import IMeal
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from ..database.database import db

unit = ["kg", "g", "L", 'cL', "mL", "unit"]


class meals:

    async def checking_meal_v2(self, meal: IMeal):
        if (meal.name == None or meal.name == ''):
            raise NameError(Custom_Error_Message.MEAL_NO_NAME.value, 403)
        if (len(meal.ingredients) <= 0):
            raise NameError(Custom_Error_Message.NO_INGREDIENTS.value, 403)
        for ingredient in meal.ingredients:
            if (ingredient.quantity <= 0):
                raise NameError(
                    Custom_Error_Message.INGREDIENT_NO_QUANTITY.value, 403)
            if (ingredient.unit not in unit):
                raise NameError(
                    Custom_Error_Message.INGREDIENT_NO_UNIT.value, 403)

    async def checking_meal(self, meal: IMeal, token: Json_web_token):
        if (meal.name == None or meal.name == ''):
            raise NameError(Custom_Error_Message.MEAL_NO_NAME.value, 403)
        var = await db["meals"].find_one({'name': meal.name, 'user_id': ObjectId(token.get_id())})
        if (var != None):
            raise NameError(
                Custom_Error_Message.MEAL_ALREADY_EXIST.value, 409)
        if (len(meal.ingredients) <= 0):
            raise NameError(Custom_Error_Message.NO_INGREDIENTS.value, 403)

    async def create_meal(self, authorization: str, meal: IMeal):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        await self.checking_meal(meal, token)
        result = await db.add_meal(meal, token)
        meal.id = str(result.inserted_id)
        return meal

    async def create_meal_v2(self, authorization: str, meal: IMeal):
        token = Json_web_token('no id')
        database = db_meals()
        token.checking_authorization(authorization)
        await self.checking_meal_v2(meal, token)
        var = await db["meals"].find_one({'name': meal.name, 'user_id': ObjectId(token.get_id())})
        if (var != None):
            raise NameError(
                Custom_Error_Message.MEAL_ALREADY_EXIST.value, 409)
        result = await database.add_meal_v2(meal, token)
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

    async def update_meal_v2(self, authorization: str, meal: IMeal, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        await self.checking_meal_v2(meal, token)
        meal.id = id
        await db.find_meal(id, token)
        await db.update_meal(id, token, meal)
        response = await db.find_meal(id, token)
        response["id"] = str(response["_id"])
        del response["_id"]
        response['user_id'] = str(response['user_id'])
        return response

    async def delete_meal(self, authorization: str, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        await db.find_meal(id, token)
        await db.remove_meal(id, token)
        return {'message': 'Meal delete'}

    async def get_meal_v2(self, authorization: str, id: str):
        token = Json_web_token('no id')
        db = db_meals()
        token.checking_authorization(authorization)
        response = await db.find_meal(id, token)
        response['_id'] = str(response['_id'])
        response['user_id'] = str(response['user_id'])
        return response

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
