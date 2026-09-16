## Client side!

import requests

my_URL = 'http://127.0.0.1:5000'

#using my browsing endpoint
def browse_section():
    response = requests.get(f"{my_URL}/browse/films")
    if response.status_code == 200: #checking my API worked
        films = response.json()
        for film in films:
            print(film['film_id'],film['title'], film['genre'], film['IMDB_rating'])
    else:
        print("Unable to retrieve films.")

def add_section():
    film = { #put user input into a dictionary
        "title" : input("Enter film title"),
        "release_year": int(input("Enter release year")),
        "genre" : input("Enter the genre"),
        "director" : input("Enter the director of this film"),
        "IMDB_rating" : input("Enter the IMDB rating of this film"),
        "runtime" : input("Enter the runtime of this film"),
        "age_rating" : input("Enter the age rating of the film") 
        }
    response = requests.post(f"{my_URL}/add/film",json=film) #pass my dict into post request
    if response.status_code == 201:
        print(response.json()["Message"]+" and Film ID is", response.json()["Film ID"]) 
    else:
        print(response.json()["Error"])

def find_section():
    try: 
        search_ID = int(input("Please enter film ID to search by"))
    except ValueError:
        print("ID must be an integer") #handles if user searches with a str
        return
    response = requests.get(f"{my_URL}/browse/films/{search_ID}")
    if response.status_code == 404:
        print(response.json()["Error"]) 
    else:
        film = response.json()
        print(f"Found! Your film is: {film['title'], film['genre']}")

def surprise_section():
    chosen_genre = input("Which genre do you want? Press enter if no preference")
    response = requests.get(f"{my_URL}/surprise?type=films&genre={chosen_genre}")
    if response.status_code == 404:
        print(response.json()["Error"])
    else:
        surprise = response.json()
        print(f"Your film to watch today is... {surprise['title'], surprise['IMDB_rating']}")

def run(): #a run function using all sections defined above
    print("Welcome to What to Watch? \n")
    user_action = input("Please choose what you would like to do: \n a) Browse films \n b) Add a Film to the database \n c) Search for a film \n d) Surprise Me! \n e) Exit")
    while user_action not in ('a','b','c','d','e'): #if user doesnt pick given options this repeats
        print("Please choose one of the given options")
        user_action = input("Please choose what you would like to do: \n a) Browse films \n b) Add a Film to the database \n c) Search for a film \n d) Surprise Me! \n e) Exit")
    while user_action != 'e': #while user chooses NOT to exit...
        #browse section
        if user_action == 'a':
            browse_section()
        #if user wants to add a film
        elif user_action == 'b':
            add_section()
        #if user wants to find a film based on its ID
        elif user_action == 'c':
            find_section()
        #if user wants to get a random selection
        elif user_action == 'd':
            surprise_section()
        user_action = input("Please choose what you would like to do: \n a) Browse films \n b) Add a Film to the database \n c) Search for a film \n d) Surprise Me! \n e) Exit")

    print("Thanks for visiting What to Watch!")
        
if __name__ == "__main__":
    run() 