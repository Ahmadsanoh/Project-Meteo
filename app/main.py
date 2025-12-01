from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import weather, activities, users, recommendations, votes_condorcet
from app.routes.votes import router as votes_router

app = FastAPI(title="Weather-Based Activities API")

# Include routers
app.include_router(weather.router)
app.include_router(activities.router)
app.include_router(users.router)
app.include_router(recommendations.router)
app.include_router(votes_condorcet.router)
app.include_router(votes_router)  

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
