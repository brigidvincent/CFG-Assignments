# Last-Minute Holiday Planner

#my plan / workflow: 
# asks the user if they want warm or cold/snowy
# the dates they plan to go
# suggests a top 3 list of countries based off that (the most popular places to visit within the weather restrictions)
# the user can then pick a country from the list,
# they will be provided with info on the country:
    # news, any holidays that take place during,
    # exchange rates/currency, suggests events to atttend
    # flight prices on the given dates 

# APIs:
# facts about country: https://restcountries.com
# news from the country: https://newsapi.org
# public holidays: https://caldays.com/api
# exchange rates/ currency conversion: https://exchangeratesapi.io/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers
# events: https://platform.seatgeek.com/
# https://apogeoapi.com/
# https://github.com/lennertVanSever/graphcountries
# https://countries.dev/docs?utm_source=chatgpt.com

import requests
import json
import datetime #additional module I've imported
import re #additional module I've imported

#Intro to program
print("Welcome to the Last-Minute Holiday Planner! \n This program will help you find the perfect holiday destination based on your preferences.\n")
print("*This program can only plan a holiday starting up to 14 days from now to ensure recommended weather is reliable*")
print("*Please note, for holidays starting on the 14th day from now, recommendations will rely mostly on historical weather data")

#storing initial information from user on their holiday preferences:
today = datetime.date.today().strftime("%d/%m/%Y")
departure_location = input("Where are you travelling from? e.g. format = 'LON' for London") #to remove this location from places to visit
chosen_weather = input("What kind of weather do you want for your holiday? Please enter a or b \n a) Sunny and warm \n b) Cool and snowy \n")

#checking user has selected from given options:
while chosen_weather not in ['a','b']:
    print("Please enter one of the given options - a for sunny and warm or b for cold and snowy")

#storing criteria for each weather type
min_temp_celsius = 20
max_temp_celsius = 10
warm_weather_codes = [0,1,2] #my weather API uses WMO weather codes, link here:
snowy_weather_codes = [71, 73, 75, 77, 85, 86]

#exception block checking holiday start date with correct format:
try:
    start_date = input("What date are you planning to leave for holiday? Please enter in the format DD/MM/YYYY")
    format = r"[0-9]+[0-9]+/[0-9]+[0-9]+/[0-9]+[0-9]+" #need to check regex here
    if start_date != format: 
        raise Exception
except:
    print("Please enter dates in given format (DD/MM/YY)")

#formatting start date in datetime compatible dates:
start_date_temp = start_date.split('/')
start_date = datetime.date(start_date_temp[2],start_date_temp[1],start_date_temp[0]).strftime("%d/%m/%Y") #maybe check if there's a neater way to do this/ does the d/m/y format work with datetime calcs?

#checking start date isn't before todays date , and no more than 14 days from today:
difference = start_date - today
if difference < 0:
    print("You cannot plan a holiday from a past date, please enter the date of today or up to 14 days in the future")
elif difference > 14:
    print("The Last Minute Holiday Planner can only plan a holiday up to 14 days in advance.")
else:
    print("Noted!")

#exception block checking length of holiday , in numerical days:
try:
    length_of_holiday = int(input("How many days do you want your holiday to last? Please enter in numerical form - e.g. 14 for 14 days"))
except ValueError:
    print("Please enter a valid format, i.e. a number for the number of days you plan to go away for.")

#working out end date of holiday:
end_date = start_date + datetime.timedelta(days=length_of_holiday)

#First use of an API! No keys needed for this one (no auth), and I'm using it to get all capital cities,
#their countries and coordinates (for my weather API) and storing them in a list of tuples
countries = requests.get("https://countries.dev/countries?fields=name,capital").json()
every_capital = []
for country in countries:
    if "capital" in country:
        name = country["name"]
        capital = country["capital"]
        city_data = requests.get(f"https://countries.dev/cities?q={capital}"
    ).json()
        latitude = city_data[0]["latitude"]
        longitude = city_data[0]["longitude"]
        every_capital.append((name, capital, latitude, longitude))


    # my logic
    # if end_date - today <= 14 days:
        # get sum of expected temps for each day between start and end date / length_of_holiday (using long and lat) 
        # get sum of weather codes for each day between start and end date / length of holiday 
        # if avg_temp > min_temp_celsius AND rounded(avg_weather_code) in warm_weather_codes: ---- maybe use a function to reuse here
            # classification_for_city = 'sunny and warm'
        # if avg_temp < max_temp_celsius AND rounded(avg_weather_code) in snowy_weather_codes:
            # classification_for_city = 'cold and snowy'
    # elif end_date - today > 14 days:
        # get sum of expected temps for each day between start and (today+14) / no.of.days between these two
        # same for weather codes as above
        # get avg temp between today+14 and end date historically (avg over 5 years)
        # same 4 weather codes
        # ratiod avg between both 
        # if ratio_avg_temp > min_temp_celsius AND rounded(ratio_avg_weather_code) in warm_weather_codes:
            # warm_city = True
        # elif ratio_avg_temp < max_temp_celsius AND rounded(ratio_avg_weather_code) in snowy_weather_codes:
            # warm_city = False
    # classification/warm_city is added to city details 
    # add no.of.visitors of the city using visitors/tourist API

    # sort through city list:
    # if chosen_weather = 'a':
        # create a new list with all classifications sunny and warm(True)
        # chosen_cities = top 3 most popular from list 
    # elif chosen_weather = 'b':
        # create a new list with all classifications cold and snowy(False)
        # chosen_cities = top 3 most popular from list 

#print(" Please the the top 3 choices for your preferences! \n chosen_cities ")
#choice = input("Please choose one from the above and we'll give you a few fun facts about your city!")





#if user chose a quieter location, chose a random 

#for warm:
#for code in weather_codes:
#   for i in range 



# country access name - pprint(countries[0]['name'])