from fastapi import APIRouter
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return [
        User(id=1, name="Alice", email="alice@example.com"),
        User(id=2, name="Bob", email="bob@example.com")
    ]
