from fastapi import FastAPI, Request
from app.routes.login import router as login
from app.routes.week import router as week
from app.routes.register import router as register
from app.routes.meal import router as meal
from app.routes.meals import router as meals
from app.routes.mealv2 import router as mealsv2
from app.routes.list import router as list
from app.routes.refresh_token import router as refresh_token
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

if __name__ == "__main__":
    load_dotenv()

app = FastAPI()
v1 = FastAPI()
v2 = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


v1.include_router(register)
v1.include_router(login)
v1.include_router(meal)
v1.include_router(meals)
v1.include_router(week)
v1.include_router(list)
v1.include_router(refresh_token)
v2.include_router(mealsv2)


app.mount("/api/v1", v1)
app.mount("/api/v2", v2)
