import requests
from config import API_KEY, BASE_URL_CURRENT
from utils import kelvin_to_celsius

def get_current_weather(city):
    try:
        params = {
            "q": city,
            "appid":API_KEY
        }
        response = requests.get(BASE_URL_CURRENT, params= params)

        if response.status_code == 404:
            return {"error": "City not found. Try again."}
        data = response.json()

        #format weather output

        weather_data = {
            "name": data["name"],
            "temp": kelvin_to_celsius(data["main"]["temp"]),
            "condition":data["weather"][0]["description"],
            "humidity":data["main"]["humidity"],
            "wind": data["wind"]["speed"]

        }
        return weather_data
    except Exception as e:
        return {"error":f"Request failed: {str(e)}"}