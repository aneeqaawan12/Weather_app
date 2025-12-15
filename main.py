from search_weather import search_city_weather
from geolocation_weather import get_weather_by_geolocation

def menu():
    print("\n ======== WEATHER APP ========")
    print("1. Search weather by city")
    print("2. Automatic location weather")
    print("3. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            search_city_weather()

        elif choice == "2":
            get_weather_by_geolocation()

        elif choice == "3":
            print("Closing Weather App. Goodbye!")

            break

        else:
            print("Invalid option. Try again. ")

if __name__ == "__main__":
    main()