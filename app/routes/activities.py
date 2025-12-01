from fastapi import APIRouter
from app.models import Activity

router = APIRouter(prefix="/activities", tags=["activities"])

@router.get("/")
def get_activities():
    # dummy list
    return [
        Activity(id=1, name="Soccer", outdoor=True),
        Activity(id=2, name="Museum Visit", outdoor=False)
    ]
