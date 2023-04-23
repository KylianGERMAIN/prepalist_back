from typing import Optional
from pydantic import BaseModel


class IUser(BaseModel):
    username: Optional[str] = ''
    email: str
    password: str
