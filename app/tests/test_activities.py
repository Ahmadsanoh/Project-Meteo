import pytest
from app.services.activity_service import list_activities, filter_activities_by_weather

def test_list_activities():
    activities = list_activities()
    assert len(activities) > 0
    assert activities[0].name is not None

def test_filter_activities_sunny():
    activities = filter_activities_by_weather("sunny")
    assert all(a.outdoor for a in activities)

def test_filter_activities_rainy():
    activities = filter_activities_by_weather("rainy")
    assert all(not a.outdoor for a in activities)
