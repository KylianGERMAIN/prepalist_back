import datetime
from app.controllers.token import Json_web_token
from app.models.user import User
from fastapi import FastAPI, Request
from pymongo import MongoClient
from app.routes.register import router as register
from dotenv import load_dotenv
import os


load_dotenv()
app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(os.getenv('JWT_SECRET_MANGO_URL'))
    app.database = app.mongodb_client[os.getenv(
        'JWT_SECRET_MANGO_COLLECTION_NAME')]


@ app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@ app.get('/')
def greeting(request: Request):
    return {'greeting': 'Hello World'}


app.include_router(register)
