from current_weather import get_current_weather
from utils import print_weather_info

def search_city_weather():
    city = input("Enter city name:  ")
    data = get_current_weather(city)
    
    if "error" in data:
        print("Error: ", data["error"])

    else:
        print_weather_info(data)