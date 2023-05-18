from pydantic import BaseModel


class IMealDay(BaseModel):
    name: str
    id: str
    serving: int


class IDay(BaseModel):
    date: str
    lunch: IMealDay
    dinner: IMealDay


class IWeek(BaseModel):
    week: list[IDay]
