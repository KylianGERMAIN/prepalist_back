
import datetime
from bson import ObjectId
from app.models.meal import IMeal
from app.utils.custom_error_message import Custom_Error_Message
from app.utils.token import Json_web_token
from ..database.database import db


class db_meals:
    async def add_meal(self, meal: IMeal, token: Json_web_token):
        day = datetime.datetime.now()
        day = day.strftime("%Y-%m-%d %H:%M:%S")
        ingredient_list = []
        meal.created_at = str(day)
        for i in meal.ingredients:
            ingredient_list.append({'ingredient': i.ingredient})
        request = await db["meals"].insert_one(
            {'user_id': ObjectId(token.get_id()), 'name': meal.name, 'ingredients': ingredient_list, 'created_at': day})
        return request

    async def remove_meal(self, id: str, token: Json_web_token):

        request = await db["meals"].delete_one(
            {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())})
        return request

    async def find_meal(self, id: str, token: Json_web_token):
        request = await db["meals"].find_one(
            {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())})
        if request == None:
            raise NameError(Custom_Error_Message.MEAL_DOES_NOT_EXIST.value)
        return request

    async def find_meals(self, token: Json_web_token):
        mymeal = list()
        async for doc in db["meals"].find({'user_id': ObjectId(
                token.get_id())}):
            doc['_id'] = str(doc['_id'])
            del doc['user_id']
            mymeal.append(doc)
        return mymeal

    async def update_meal(self, id: str, token: Json_web_token, meal: IMeal):
        filter = {'_id': ObjectId(id), 'user_id': ObjectId(token.get_id())}
        ingredient_list = []
        day = datetime.datetime.now()
        day = day.strftime("%Y-%m-%d %H:%M:%S")
        for i in meal.ingredients:
            ingredient_list.append({'ingredient': i.ingredient})
        new_values = {"$set": {'name': str(meal.name), 'ingredients':
                               ingredient_list}}
        request = await db["meals"].update_one(filter, new_values)
        return request
