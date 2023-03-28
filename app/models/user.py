from pydantic import BaseModel


class IUser(BaseModel):
    username: str
    email: str
    password: str
