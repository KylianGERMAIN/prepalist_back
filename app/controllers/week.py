import datetime
from bson import ObjectId
from app.models.week import IWeek
from app.utils.custom_error_message import Custom_Error_Message
from app.utils.token import Json_web_token
from ..database.database import db
import random


class week:

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
            x['lunch'] = {'name': '', 'id': '', 'serving': 1}
            x['dinner'] = {'name': '', 'id': '', 'serving': 1}
        return (next_week)

    async def next_week_add_meal(self, next_week: list, token: Json_web_token):
        var = await db["meals"].count_documents({'user_id': ObjectId(token.get_id())}) - 1
        if (var < 9):
            raise NameError(Custom_Error_Message.NO_ENOUGH_MEALS.value, 403)
        random_nb = random.randint(1, var)
        mymeal = list()
        async for doc in db["meals"].find({'user_id': ObjectId(
                token.get_id())}):
            mymeal.append(doc)
        myweek_meal = list()
        for i in range(7):
            random_nb = random.randint(0, var)
            myweek_meal.append(
                {'name': mymeal[random_nb]['name'], 'id': str((mymeal[random_nb]['_id'])), 'serving': 1})

            if (i == 0):
                next_week[i + 1]['lunch'] = myweek_meal[i]
                next_week[i]['dinner'] = myweek_meal[i]
                mymeal.pop(random_nb)
            elif (i > 0 and i < 6):
                next_week[i + 1]['lunch'] = myweek_meal[i]
                next_week[i]['dinner'] = myweek_meal[i]
                mymeal.pop(random_nb)
            else:
                next_week[i]['dinner'] = myweek_meal[i]
                mymeal.pop(random_nb)
            var = var - 1
        return (next_week)

    async def add_week(self, new_week: IWeek, token: Json_web_token):
        if (len(new_week.week) != 7):
            raise NameError(Custom_Error_Message.NO_ENOUGH_DAYS.value, 403)
        json_week = new_week.dict()
        request = await db["weeks"].find_one(
            {'user_id': ObjectId(token.get_id())})
        if (request == None):
            await db["weeks"].insert_one({
                'user_id': ObjectId(token.get_id()),
                'date': json_week["week"]
            })
        else:
            await db["weeks"].delete_one({'user_id': ObjectId(token.get_id())})
            await db["weeks"].insert_one({
                'user_id': ObjectId(token.get_id()),
                'date': json_week["week"]
            })

    async def create_my_week_verification(self, authorization: str, new_week: IWeek):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        await self.add_week(new_week, token)
        return new_week

    async def generate_my_week(self, authorization: str):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        today = str(datetime.date.today())
        start_end = await self.get_start_end_of_week(today)
        first_day_of_next_day = await self.get_next_day(start_end[1])
        next_week = await self.set_next_week_date(first_day_of_next_day)
        next_week = await self.next_week_create_meal(next_week)
        next_week = await self.next_week_add_meal(next_week, token)
        return (next_week)

    async def get_my_week(self, authorization: str):
        token = Json_web_token('no id')
        token.checking_authorization(authorization)
        request = await db["weeks"].find_one(
            {'user_id': ObjectId(token.get_id())})
        if (request == None):
            raise NameError(Custom_Error_Message.NO_WEEK.value, 403)
        return {'_id': str(request['_id']), 'date': request['date']}
