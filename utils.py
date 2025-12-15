def kelvin_to_celsius(temp_k):
    return round(temp_k - 273.15,2)

def print_weather_info(data):
    print("\n--- Weather Report ---")
    print("City: ", data["name"])
    print("Temperature (°C):", data["temp"])
    print("Condition:", data["condition"])
    print("Humidity:", data["humidity"])
    print("Wind speed(m/s):", data["wind"])
    print("---------------------------\n")