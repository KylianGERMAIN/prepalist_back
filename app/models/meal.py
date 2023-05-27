from pydantic import BaseModel


class IIngredient(BaseModel):
    ingredient: str


class IMeal(BaseModel):
    id: str | None
    name: str
    ingredients: list[IIngredient] = []
    created_at: str | None


class IIngredient_V2(BaseModel):
    ingredient: str
    quantity: float
    unit: str


class IMeal_V2(BaseModel):
    id: str | None
    name: str
    ingredients: list[IIngredient_V2] = []
    created_at: str | None
