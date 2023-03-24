
from pydantic import BaseModel


class Response_tokens(BaseModel):
    refresh_token: str
    access_token: str
    expires_in: str
    token_type: str
