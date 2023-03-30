import datetime
import os
from app.utils.password import Crypt_password
from app.utils.token import Json_web_token
from app.utils.custom_error_message import Custom_Error_Message
from fastapi import HTTPException


async def start_end_of_week(day: str):
    dt = datetime.datetime.strptime(day, '%Y-%m-%d')
    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=6)
    start = datetime.datetime.strptime(
        str(start), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    end = datetime.datetime.strptime(
        str(end), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    return (str(start), str(end))


async def next_day(day: str):
    dt = datetime.datetime.strptime(str(day), '%Y-%m-%d')
    date_plus_1 = dt + datetime.timedelta(days=1)
    next_day = datetime.datetime.strptime(
        str(date_plus_1), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    return str(next_day)


async def next_week_fun(first_day_of_next_day: str):
    result = []
    dt = datetime.datetime.strptime(str(first_day_of_next_day), '%Y-%m-%d')
    for x in range(7):
        date_plus_7 = dt + datetime.timedelta(days=x)
        result.append({"date": str(date_plus_7)})
    return result


async def next_week_create_meal(next_week: list):
    for x in next_week:
        x['lunch'] = ''
        x['dinner'] = ''
    return (next_week)


async def create_my_week_verification():
    today = str(datetime.date.today())
    start_end = await start_end_of_week(today)
    first_day_of_next_day = await next_day(start_end[1])
    next_week = await next_week_fun(first_day_of_next_day)
    next_week = await next_week_create_meal(next_week)
    print(next_week)
    return (next_week)
