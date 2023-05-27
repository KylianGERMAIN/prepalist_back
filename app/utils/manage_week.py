import datetime
import random
from bson import ObjectId
from app.utils.token import Json_web_token
from ..database.database import db


class Manage_week:

    def __init__(self):
        self.__today = str(datetime.date.today())

    def get_end_of_week(self):
        dt = datetime.datetime.strptime(self.__today, '%Y-%m-%d')
        start = dt - datetime.timedelta(days=dt.weekday())
        end = start + datetime.timedelta(days=6)
        end = datetime.datetime.strptime(
            str(end), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        return (str(end))

    async def get_next_day(day: str):
        dt = datetime.datetime.strptime(day, '%Y-%m-%d')
        date_plus_1 = dt + datetime.timedelta(days=1)
        next_day = datetime.datetime.strptime(
            str(date_plus_1), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
        return str(next_day)

    async def create_next_week_object(first_day_of_next_week: str):
        result = []
        dt = datetime.datetime.strptime(
            str(first_day_of_next_week), '%Y-%m-%d')
        for x in range(7):
            date_plus_7 = dt + datetime.timedelta(days=x)
            result.append({"date": str(date_plus_7)})
        return result

    async def create_next_week_meal(next_week: list):
        for x in next_week:
            x['lunch'] = ''
            x['dinner'] = ''
        return (next_week)

    async def next_week_add_meal(next_week: list, token: Json_web_token):
        var = await db["meals"].count_documents({'user_id': ObjectId(token.get_id())}) - 1
        random_nb = random.randint(1, var)
        mymeal = list()
        async for doc in db["meals"].find({'user_id': ObjectId(
                token.get_id())}):
            mymeal.append(doc)
        myweek_meal = list()
        for i in range(7):
            random_nb = random.randint(0, var)
            myweek_meal.append(mymeal[random_nb]['name'])
            if (i != 6):
                next_week[i]['dinner'] = myweek_meal[i]
                next_week[i + 1]['lunch'] = myweek_meal[i]
                mymeal.pop(random_nb)
            else:
                next_week[i]['dinner'] = myweek_meal[i]
                mymeal.pop(random_nb)
            var = var - 1
        return (next_week)
