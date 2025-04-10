from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    username: str
    balance: float

class Fish(BaseModel):
    name: str
    price: float
    cathced: str