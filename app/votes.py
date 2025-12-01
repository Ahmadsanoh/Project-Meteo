from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Vote

router = APIRouter(prefix="/votes", tags=["votes"])

# ------------------------
# In-memory votes list (for 15 users)
# Each user ranks activities by ID (example: "1,2,3")
# ------------------------
votes_db: List[Vote] = [
    Vote(id=1, user_id=1, ranking="1,2,3"),
    Vote(id=2, user_id=2, ranking="2,3,1"),
    Vote(id=3, user_id=3, ranking="3,1,2"),
    Vote(id=4, user_id=4, ranking="1,3,2"),
    Vote(id=5, user_id=5, ranking="2,1,3"),
    Vote(id=6, user_id=6, ranking="3,2,1"),
    Vote(id=7, user_id=7, ranking="1,2,3"),
    Vote(id=8, user_id=8, ranking="2,3,1"),
    Vote(id=9, user_id=9, ranking="3,1,2"),
    Vote(id=10, user_id=10, ranking="1,3,2"),
    Vote(id=11, user_id=11, ranking="2,1,3"),
    Vote(id=12, user_id=12, ranking="3,2,1"),
    Vote(id=13, user_id=13, ranking="1,2,3"),
    Vote(id=14, user_id=14, ranking="2,3,1"),
    Vote(id=15, user_id=15, ranking="3,1,2"),
]

# ------------------------
# GET all votes
# ------------------------
@router.get("/", response_model=List[Vote])
def get_votes():
    return votes_db

# ------------------------
# SUBMIT a vote
# ------------------------
@router.post("/", response_model=Vote)
def submit_vote(vote: Vote):
    # Check if user_id is valid (1-15)
    if not (1 <= vote.user_id <= 15):
        raise HTTPException(status_code=404, detail=f"User ID {vote.user_id} not found")
    
    # Assign an incremental ID to the vote
    vote.id = len(votes_db) + 1
    votes_db.append(vote)
    return vote
