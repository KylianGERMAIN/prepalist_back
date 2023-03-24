from fastapi import FastAPI, Request
from app.routes.register import router as register
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

app = FastAPI()


@app.get('/')
def greeting(request: Request):
    return {'greeting': 'Hello World'}


app.include_router(register)
