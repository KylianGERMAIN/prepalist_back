from fastapi import FastAPI, Request
from app.routes.my_week import router as my_week
from app.routes.login import router as login
from app.routes.create_my_week import router as create_my_week
from app.routes.register import router as register
from app.routes.meal import router as meal
from app.routes.meals import router as meals
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

if __name__ == "__main__":
    load_dotenv()

app = FastAPI()
v1 = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@v1.get('/lol')
def greeting(request: Request):
    return {'greeting': 'Hello World'}


v1.include_router(register)
v1.include_router(login)
v1.include_router(meal)
v1.include_router(meals)
v1.include_router(create_my_week)
v1.include_router(my_week)


app.mount("/api/v1", v1)
