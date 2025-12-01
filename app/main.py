from fastapi import FastAPI
from app.routes import weather, activities, users

app = FastAPI(title="Weather-Based Activities API")

# Include routers
app.include_router(weather.router)
app.include_router(activities.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Hello World!"}
