from pydantic import BaseModel


class Ingredient(BaseModel):
    ingredient: str


class Meal(BaseModel):
    id: str | None
    name: str
    ingredients: list[Ingredient] = []
