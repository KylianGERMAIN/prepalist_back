from pydantic import BaseModel


class Ingredient(BaseModel):
    ingredient: str


class Meal(BaseModel):
    name: str
    ingredients: list[Ingredient] = []
