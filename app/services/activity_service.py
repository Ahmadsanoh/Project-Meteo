from typing import List
from app.models import Activity

# Temporary in-memory activities (15 total)
activities_db: List[Activity] = [
    Activity(id=1, name="Museum Visit", outdoor=False, description="Local art museum"),
    Activity(id=2, name="Park Walk", outdoor=True, description="City central park"),
    Activity(id=3, name="Swimming Pool", outdoor=False, description="Indoor swimming pool"),
    Activity(id=4, name="Soccer Match", outdoor=True, description="Community soccer game"),
    Activity(id=5, name="Art Workshop", outdoor=False, description="Painting and crafts"),
    Activity(id=6, name="Hiking", outdoor=True, description="Trail in nearby forest"),
    Activity(id=7, name="Bowling", outdoor=False, description="Indoor bowling alley"),
    Activity(id=8, name="Tennis", outdoor=True, description="Outdoor tennis courts"),
    Activity(id=9, name="Cooking Class", outdoor=False, description="Culinary school workshop"),
    Activity(id=10, name="Cycling", outdoor=True, description="City bike tour"),
    Activity(id=11, name="Library Visit", outdoor=False, description="City public library"),
    Activity(id=12, name="Kayaking", outdoor=True, description="River kayaking adventure"),
    Activity(id=13, name="Yoga", outdoor=True, description="Outdoor yoga in the park"),
    Activity(id=14, name="Escape Room", outdoor=False, description="Indoor puzzle game"),
    Activity(id=15, name="Gardening Workshop", outdoor=True, description="Community garden activity")
]

def list_activities() -> List[Activity]:
    return activities_db

def filter_activities_by_weather(weather_condition: str) -> List[Activity]:
    """
    Return outdoor activities for sunny/clear weather,
    indoor activities for other weather conditions.
    """
    if weather_condition.lower() in ["sunny", "clear"]:
        return [a for a in activities_db if a.outdoor]
    return [a for a in activities_db if not a.outdoor]
