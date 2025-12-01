from fastapi import APIRouter
from typing import List
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[User])
def get_users():
    return [
        User(id=1, name="Alice", email="alice@example.com", prefers_outdoor=True, tags="sport,museum"),
        User(id=2, name="Bob", email="bob@example.com", prefers_outdoor=False, tags="museum,art"),
        User(id=3, name="Charlie", email="charlie@example.com", prefers_outdoor=True, tags="sport,swimming"),
        User(id=4, name="David", email="david@example.com", prefers_outdoor=True, tags="park,hiking"),
        User(id=5, name="Eve", email="eve@example.com", prefers_outdoor=False, tags="museum,art"),
        User(id=6, name="Frank", email="frank@example.com", prefers_outdoor=True, tags="sport,cycling"),
        User(id=7, name="Grace", email="grace@example.com", prefers_outdoor=False, tags="museum,library"),
        User(id=8, name="Hannah", email="hannah@example.com", prefers_outdoor=True, tags="park,swimming"),
        User(id=9, name="Ivan", email="ivan@example.com", prefers_outdoor=False, tags="museum,concert"),
        User(id=10, name="Judy", email="judy@example.com", prefers_outdoor=True, tags="sport,tennis"),
        User(id=11, name="Karl", email="karl@example.com", prefers_outdoor=False, tags="museum,art"),
        User(id=12, name="Laura", email="laura@example.com", prefers_outdoor=True, tags="hiking,park"),
        User(id=13, name="Mallory", email="mallory@example.com", prefers_outdoor=False, tags="library,museum"),
        User(id=14, name="Niaj", email="niaj@example.com", prefers_outdoor=True, tags="cycling,sport"),
        User(id=15, name="Olivia", email="olivia@example.com", prefers_outdoor=False, tags="concert,art")
    ]
