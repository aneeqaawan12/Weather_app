import geocoder
from current_weather import get_current_weather
from utils import print_weather_info

def get_weather_by_geolocation():
    print("Detecting your location...")

    g = geocoder.ip("me")

    if g.ok:
        city = g.city
        print(f"Detected city: {city}")

        data = get_current_weather(city)
        if "error" in data:
            print("Error: ", data["error"])
        else:
            print_weather_info(data)

    else:
        print("Could not detect your location. ")


if __name__ == "__main__":
    get_weather_by_geolocation()