import requests
import json

countries = requests.get("https://countries.dev/countries?fields=name,capital").json()

for country in countries:
    if "capital" not in country:
        print(country)