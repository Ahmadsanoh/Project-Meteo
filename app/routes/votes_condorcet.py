from fastapi import APIRouter
from typing import List, Dict
from app.models import Activity
from app.services.activity_service import list_activities
from app.routes.votes import votes_db


router = APIRouter(prefix="/votes", tags=["votes"])

# ------------------------
# Condorcet Winner endpoint
# ------------------------
@router.get("/condorcet-winner/", response_model=List[Activity])
def get_condorcet_winner():
    """
    Computes the Condorcet winner from all votes in votes_db.
    Returns one or more activities in case of tie.
    """
    activities = list_activities()
    activity_ids = [a.id for a in activities]

    # No votes yet
    if not votes_db:
        return []

    # Initialize pairwise win counts
    pairwise_wins: Dict[int, Dict[int, int]] = {i: {j: 0 for j in activity_ids if j != i} for i in activity_ids}

    # Count pairwise wins
    for vote in votes_db:
        ranked_ids = [int(x) for x in vote.ranking.split(",")]
        for i, a in enumerate(ranked_ids):
            for b in ranked_ids[i + 1:]:
                pairwise_wins[a][b] += 1

    # Find Condorcet winner(s)
    winner_ids = []
    for a in activity_ids:
        wins_all = True
        for b in activity_ids:
            if a == b:
                continue
            if pairwise_wins[a][b] <= pairwise_wins[b][a]:
                wins_all = False
                break
        if wins_all:
            winner_ids.append(a)

    # Return activities matching winner_ids
    winners = [a for a in activities if a.id in winner_ids]
    return winners
