import os
from dotenv import load_dotenv

# Load the .env file inside the app folder
load_dotenv(dotenv_path="app/.env")

# Read API key
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
DEFAULT_CITY = "Paris"

# Debugging: check if the key is loaded (remove before pushing to GitHub)
print("Loaded OpenWeather API key:", OPENWEATHER_API_KEY)
