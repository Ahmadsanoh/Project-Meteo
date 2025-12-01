from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

# ------------------------
# WEATHER
# ------------------------
class Weather(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    temperature: float
    condition: str
    air_quality: Optional[str] = None


# ------------------------
# ACTIVITY
# ------------------------
class Activity(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    outdoor: bool = True


# ------------------------
# USER
# ------------------------
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    prefers_outdoor: Optional[bool] = None
    tags: Optional[str] = None  # CSV: "sport, kids, museum"
    votes: List["Vote"] = Relationship(back_populates="user")


# ------------------------
# VOTE (Condorcet input)
# ------------------------
class Vote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    ranking: str  # CSV of activity IDs e.g. "3,1,2"
    user: Optional[User] = Relationship(back_populates="votes")


# ------------------------
# RESPONSE MODEL: WEATHER + ACTIVITIES
# ------------------------
class WeatherActivitiesResponse(SQLModel):
    weather: Optional[Weather]
    activities: List[Activity] = []
