## FILM API - HOW TO RUN 

### Intro
<p>This is an API that interacts with a database of films. It allows users to:
- browse all films in the database
- look up a specific film using its ID
- add a film if they wish
- use the Surprise Me! function that fetches a random film (based on a genre if the user has specified this).</p>
<br>
<p>The API and its routes are in the app.py file, and the client side is within the main.py file which demonstrates how a user might interact with the API.</p>

## Breakdown of files
- **app.py** : This is where the Flask API and its routes live.
- **main.py** : Contains the client side which communicates with the API
- **config.py** : Contains the application's configuration settings - in this case retrieves the database credentials from the .env file (instead of hardcoding this into the script). *you will need a complementary .env file with the specific DB HOST and DB password details*
- **.env** – As mentioned above, stores database credentials such as the host, username and password.This file should be kept private (!!) not be committed to a public repository.
- **database.py** : Contains the initial setup of the database used by the API. This only needs to be run *once* at the start of running the app.
- **db_utils.py** : Where I set up the get_connection() function, so that it can be used throughout to connect to the database.
- **helper_functions.py** : This includes all the functions my API uses to query and interact with the database, stored separately from app.py to avoid cluttering my flask app.

## Installation Requirements
To run this application, Python 3 and MySQL are required. You will also need the modules detailed in *requirements.txt*, which you can download within a venv:
> python3 -m venv .venv
> source .venv/bin/activate

## How to set up
<p>First, you need to set up a config.py file (or use the one in this project), and alongside it, a .env file, which the config file will use to get the credentials needed to run...</p>
<p>Your .env file should look like this: </p>
DB_HOST = localhost
DB_PORT = your_port_number
> DB_USER = your_user_name
> DB_PASSWORD = your_password
> DB_NAME = entertainment_db 

*The values above are placeholders, and you should replace with your own credentials.*
*The database name should be initially commented out during database creation (when running database.py)*

## How to Run
<p> Next, the following files should be run in the coming order:</p>
- First, run **database.py** to set up the needed database, and only *once* 
> python3 database.py
- Next, **app.py** should be run to start up the API - this should provide you with a message with a link (e.g. Running on http://127.0.0.1:5000 ). One clicked (Ctrl+click or Cmd+click), you should see a welcome message on a website.
> python3 app.py
- Finally, in a *new terminal* , while the other terminal is running with **app.py**, run **main.py**. This will simulate the client side and show what you can do with my API.
> python3 main.py

<p> Hope you enjoy! </p>
