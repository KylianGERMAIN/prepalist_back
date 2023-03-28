from pydantic import BaseModel


class IIngredient(BaseModel):
    ingredient: str


class IMeal(BaseModel):
    id: str | None
    name: str
    ingredients: list[IIngredient] = []
