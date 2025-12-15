import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

#Base url
BASE_URL_CURRENT = "https://api.openweatherapp.org/data/2.5/weather"