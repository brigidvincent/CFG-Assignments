# Last-Minute Holiday Planner

# My Final Plan / Workflow: 
    # asks the user if they want a warm or cold/snowy holiday,
    # the length of the holiday 
    # the program then suggests a top 3 list of countries based off user's answers

# APIs used:
# https://www.weatherapi.com - I used this to grab the weather forecast of cities (namely avg temp and conditions),
    # https://www.weatherapi.com/docs/ details how to request data, creating an account through here will provide you with an API key

# https://countries.dev/ - I used this to grab a list of capital cities to check the weather of, no authentication/ API key needed 
    # https://countries.dev/docs details how to request data and which fields


import requests
import json
import datetime
import time
import random #for a random index for suggestion at end

#to keep API keys private/ not hard coded - had to look this up as I was a bit confused
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

#Intro to program
print("\n Welcome to the Last-Minute Holiday Planner! \n This program will help you find the perfect holiday destination based on your preferences.\n")
print("This will provide recommendations for a holiday starting from tomorrow, and ending up to 14 days from now (to ensure recommended weather is reliable) \n")

#storing user's holiday preference:
chosen_weather = input("What kind of weather do you want for your holiday? Please enter a or b \n a) Sunny and warm \n b) Cool and snowy \n")

#checking user has selected from given options:
while chosen_weather not in ['a','b']:
    print("Please enter one of the given options - a for sunny and warm or b for cold and snowy")
    chosen_weather = input("What kind of weather do you want for your holiday? Please enter a or b \n a) Sunny and warm \n b) Cool and snowy \n")

#set some default values
max_temp_celsius = 30
min_temp_celsius = -10

#asking user for a max/min temp depending on their option to help filter suggestions later
if chosen_weather == 'a':
    while True:
        try:
            max_temp_celsius = int(input("Please indicate the hottest weather you can tolerate: "))
            if max_temp_celsius < 20:
                print("Please enter a temperature of 20°C or above, or change your preference to cold and snowy")
            else:
                break
        except ValueError:
            print("Please enter a valid temperature number, e.g. 26")
elif chosen_weather == 'b':
    while True:
        try:
            min_temp_celsius = int(input("Please indicate the coldest temp you can tolerate: "))
            if min_temp_celsius > 5:
                print("Please enter a temperature of 5°C or below, or change your preference to warm and sunny")
            else:
                break
        except ValueError:
            print("Please enter a valid temperature number, e.g. -5")


#exception block checking length of holiday is a valid number and between 1-14 days
while True:
    try:
        length_of_holiday = int(input("How many days do you want your holiday to last (starting tomorrow)? Please enter a number, e.g. 6: "))
        if length_of_holiday < 1 or length_of_holiday > 14:
            raise ValueError
        break

    except ValueError:
        print("Please enter a number between 1 and 14.")

#recording key dates
today = datetime.date.today()
start_date = today + datetime.timedelta(days=1)

# function that gets weather data for a given capital city (using mmy first API), using start date and length of holiday given by user
# returns the average temperature over the holiday and the sunny/snow score % :

def get_weather_score(capital, country):
    weather = requests.get(
    f"https://api.weatherapi.com/v1/forecast.json"
    f"?key={API_KEY}"
    f"&q={capital},{country}" 
    f"&days={length_of_holiday}" 
    f"&dt={start_date}",
).json() #gets the weather forecast for given city for length_of_holiday amount of days, starting from start_date (tomorrow)
    
    weather_for_location = [] #empty list

    for forecast_day in weather["forecast"]["forecastday"]: #iterating over each day I've grabbed the weather info of
        day = forecast_day["day"]
        weather_for_location.append({ #taking relevant info (below are the fields I've grabbed) for each day of the weather info got from API above
            "city": weather["location"]["name"],
            "country": weather["location"]["country"],
            "date": forecast_day["date"],
            "avg_temp": day["avgtemp_c"],
            "condition": day["condition"]["text"]
            })

    avg_temp_overall = sum(day["avg_temp"] for day in weather_for_location) / len(weather_for_location) 
    
    #look for sunny days of location
    sunny_score = 0
    for day in weather_for_location:
        if day["condition"] in ["Sunny","Clear"]:
            sunny_score += 1
        elif day["condition"]=="Partly cloudy":
            sunny_score += 0.5

    sunny_score_percentage = (sunny_score / len(weather_for_location)) * 100
    
    #look for snowy days of location
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

#empty lists to add suggested countries to when compared to criteria (below)
warm_suggested_countries=[]
cold_suggested_countries=[]

#Countries API 
#to get a list of all countries + their capital cities in the world:
countries = requests.get(
    "https://countries.dev/countries?fields=name,capital"
).json() #this is a list of dictionaries

#now to look at every city and determine its score:
for country in countries:
    if "capital" in country: #some countries don't have capitals e.g. Antarctica!
        print(f"Checking {country['name']}...") #this part takes a sec so added this to know program isn't crashing
        weather_score = get_weather_score(
            country["capital"],
            country["name"]
        )
        country.update(weather_score) #adds the weather score into each dictionary/city

        #adding countries to suggested using temp range set by user:
        if country["avg_temp_overall"]>20 and country["avg_temp_overall"]<max_temp_celsius: 
            warm_suggested_countries.append(country)
        elif country["avg_temp_overall"]<5 and country["avg_temp_overall"]>min_temp_celsius:
            cold_suggested_countries.append(country)

#ordering suggested countries in descending order (so that snowiest/sunniest locations are first in the list)
warm_suggested_countries=sorted(warm_suggested_countries, key=lambda city: city["sunny_score_percentage"], reverse=True) 
cold_suggested_countries=sorted(cold_suggested_countries, key=lambda city: city["snowy_score_percentage"], reverse=True)

if chosen_weather == 'a': #if sunny was picked...
    final_reccomendation = []
    for i in range(3): #3 recommendations
        random_index = random.randint(0, len(warm_suggested_countries)//2) #randomly selects a location in the first half of the list where the sunniest locations are
        final_reccomendation.append(warm_suggested_countries[random_index])
    print(f"We suggest the following locations! \n a){final_reccomendation[0]} \n b){final_reccomendation[1]} \n c){final_reccomendation[2]}\n")

elif chosen_weather == 'b': #same process with snowy locations
    final_reccomendation = []
    for i in range(3): 
        random_index = random.randint(0, len(cold_suggested_countries)//2)
        final_reccomendation.append(cold_suggested_countries[random_index])
    print(f"We suggest the following locations! \n a){final_reccomendation[0]} \n b){final_reccomendation[1]} \n c){final_reccomendation[2]}\n")
