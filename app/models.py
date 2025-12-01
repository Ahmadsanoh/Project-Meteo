from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

# Weather model
class Weather(SQLModel):
    date: date
    temperature: float
    condition: str  # e.g., "sunny", "rainy"

# Activity model
class Activity(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    outdoor: bool  # True = outdoor activity, False = indoor
    description: Optional[str] = None

# User model
class User(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
