from app.votes import votes_db
from app.models import Vote

def test_submit_vote():
    votes_db.clear()
    vote = Vote(id=1, user_id=1, ranking="1,2,3")
    votes_db.append(vote)
    assert len(votes_db) == 1
    assert votes_db[0].user_id == 1
