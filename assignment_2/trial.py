#to try small parts of code outside of main python file

import requests
import json
import time
import datetime

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

#hard coding for now to see if code works

length_of_holiday = 7 
start_date= "2026-08-18"

countries = requests.get(
    "https://countries.dev/countries?fields=name,capital"
).json()

def get_weather_data(capital, country):
    weather = requests.get(
    f"https://api.weatherapi.com/v1/forecast.json"
    f"?key={API_KEY}"
    f"&q={capital},{country}"
    f"&days={length_of_holiday}"
    f"&dt={start_date}"
).json()
    weather_for_location = []

    for forecast_day in weather["forecast"]["forecastday"]:
        day = forecast_day["day"]

        weather_for_location.append({
            "city": weather["location"]["name"],
            "country": weather["location"]["country"],
            "date": forecast_day["date"],
            "avg_temp": day["avgtemp_c"],
            "condition": day["condition"]["text"]
        })

    avg_temp_overall = sum(day["avg_temp"] for day in weather_for_location) / len(weather_for_location)

    #look for sunny days
    sunny_score = 0

    for day in weather_for_location:
        if day["condition"] in ["Sunny","Clear","Partly cloudy"]:
            sunny_score += 1

    sunny_score_percentage = (sunny_score / len(weather_for_location)) * 100

    #look for snowy days 
    snowy_score = 0

    for day in weather_for_location:
        if day["condition"] in ["Light snow", "Moderate snow", "Heavy snow"]:
            snowy_score += 1

    snowy_score_percentage = (snowy_score / len(weather_for_location)) * 100

    return {
        "avg_temp_overall": avg_temp_overall,
        "sunny_score_percentage": sunny_score_percentage,
        "snowy_score_percentage": snowy_score_percentage
    }

print("Paris, France:", get_weather_data('Paris','France'))

today = datetime.date.today()
start_date = today + datetime.timedelta(days=1)

print(start_date)


# for location in countries:
#     if "capital" in location:
#         capital = location["capital"]
#         country = location["name"]
#         start_date = "2026-08-17"
#         length_of_holiday = 7
#         weather_data = get_weather_data(capital, country, start_date, length_of_holiday)
#         print(f"Weather data for {capital}, {country}:")
#         pprint(weather_data)
#         time.sleep(1)  # To avoid hitting the API rate limit
