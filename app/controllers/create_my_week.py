import datetime

from bson import ObjectId
from fastapi import HTTPException
from app.utils.custom_error_message import Custom_Error_Message
from app.utils.token import Json_web_token
from ..database.database import db
import random


class my_week:

    async def get_start_end_of_week(self, day: str):
        dt = datetime.datetime.strptime(day, '%Y-%m-%d')
        start = dt - datetime.timedelta(days=dt.weekday())
        end = start + datetime.timedelta(days=6)
        start = datetime.datetime.strptime(
            str(start), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        end = datetime.datetime.strptime(
            str(end), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        return (str(start), str(end))

    async def get_next_day(self, day: str):
        dt = datetime.datetime.strptime(str(day), '%Y-%m-%d')
        date_plus_1 = dt + datetime.timedelta(days=1)
        next_day = datetime.datetime.strptime(
            str(date_plus_1), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        return str(next_day)

    async def set_next_week_date(self, first_day_of_next_day: str):
        result = []
        dt = datetime.datetime.strptime(str(first_day_of_next_day), '%Y-%m-%d')
        for x in range(7):
            date_plus_7 = dt + datetime.timedelta(days=x)
            result.append({"date": str(date_plus_7)})
        return result

    async def next_week_create_meal(self, next_week: list):
        for x in next_week:
            x['lunch'] = {'name': '', 'id': ''}
            x['dinner'] = {'name': '', 'id': ''}
        return (next_week)

    async def next_week_add_meal(self, next_week: list, token: Json_web_token):
        var = await db["meals"].count_documents({'user_id': ObjectId(token.get_id())}) - 1
        if (var < 9):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.NO_ENOUGH_MEALS.value)
        random_nb = random.randint(1, var)
        mymeal = list()
        async for doc in db["meals"].find({'user_id': ObjectId(
                token.get_id())}):
            mymeal.append(doc)
        myweek_meal = list()
        for i in range(7):
            random_nb = random.randint(0, var)
            myweek_meal.append(
                {'name': mymeal[random_nb]['name'], 'id': str((mymeal[random_nb]['_id']))})
            if (i != 6):
                next_week[i]['dinner'] = myweek_meal[i]
                next_week[i + 1]['lunch'] = myweek_meal[i]
                mymeal.pop(random_nb)
            elif (i == 0):
                next_week[i]['dinner'] = myweek_meal[i]
                mymeal.pop(random_nb)
            else:
                next_week[i]['lunch'] = myweek_meal[i]
                mymeal.pop(random_nb)
            var = var - 1
        return (next_week)

    async def add_week(self, next_week: list, token: Json_web_token):
        request = await db["weeks"].find_one(
            {'user_id': ObjectId(token.get_id())})
        if (request == None):
            await db["weeks"].insert_one({
                'user_id': ObjectId(token.get_id()),
                'date': next_week
            })
        else:
            await db["weeks"].delete_one({'user_id': ObjectId(token.get_id())})
            await db["weeks"].insert_one({
                'user_id': ObjectId(token.get_id()),
                'date': next_week
            })

    async def create_my_week_verification(self, authorization: str):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        today = str(datetime.date.today())
        start_end = await self.get_start_end_of_week(today)
        first_day_of_next_day = await self.get_next_day(start_end[1])
        next_week = await self.set_next_week_date(first_day_of_next_day)
        next_week = await self.next_week_create_meal(next_week)

        next_week = await self.next_week_add_meal(next_week, token)
        await self.add_week(next_week, token)
        return (next_week)

    async def get_my_week(self, authorization: str):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        request = await db["weeks"].find_one(
            {'user_id': ObjectId(token.get_id())})
        if (request == None):
            raise HTTPException(
                status_code=403, detail=Custom_Error_Message.NO_WEEK.value)
        return {'_id': str(request['_id']), 'date': request['date']}
