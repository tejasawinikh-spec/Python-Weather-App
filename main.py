import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_KEY")

# OpenWeather API URLs
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


# Function to get current weather
def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n========== CURRENT WEATHER ==========")
            print("City:", data["name"])
            print("Temperature:", temperature, "°C")
            print("Humidity:", humidity, "%")
            print("Weather:", description)
            print("Wind Speed:", wind_speed, "m/s")
            print("=====================================")

            return True

        elif response.status_code == 404:
            print("City not found. Please enter a valid city.")

        elif response.status_code == 401:
            print("Invalid API key or API key not activated yet.")

        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException:
        print("Unable to connect. Please check your internet connection.")

    return False


# Function to get 5-day weather forecast
def get_forecast(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            print("\n========== 5-DAY WEATHER FORECAST ==========")

            displayed_dates = set()

            for item in data["list"]:

                date = item["dt_txt"].split(" ")[0]

                if date not in displayed_dates:

                    temperature = item["main"]["temp"]
                    description = item["weather"][0]["description"]

                    print("\nDate:", date)
                    print("Temperature:", temperature, "°C")
                    print("Weather:", description)

                    displayed_dates.add(date)

            print("\n============================================")

        elif response.status_code == 401:
            print("Invalid API key or API key not activated yet.")

        elif response.status_code == 404:
            print("City not found.")

        else:
            print("Error:", response.status_code)

    except requests.exceptions.RequestException:
        print("Unable to connect to the weather service.")


# Main program
if __name__ == "__main__":

    print("\n================================")
    print("       PYTHON WEATHER APP")
    print("================================")

    if not API_KEY:
        print("Error: API key not found.")
        print("Please check your .env file.")

    else:
        city = input("\nEnter city name: ").strip()

        if city:
            if get_weather(city):
                get_forecast(city)
        else:
            print("Please enter a city name.")

    print("\nThank you for using Weather App!")