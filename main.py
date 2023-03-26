from fastapi import FastAPI, Request
from app.routes.login import router as login
from app.routes.register import router as register
from app.routes.meal import router as meal
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

app = FastAPI()


@app.get('/')
def greeting(request: Request):
    return {'greeting': 'Hello World'}


app.include_router(register)
app.include_router(login)
app.include_router(meal)
