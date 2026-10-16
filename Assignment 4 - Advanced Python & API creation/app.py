from flask import Flask, jsonify, request
from helper_functions import get_all_films, get_film_by_id, insert_film, surprise_me

app = Flask(__name__)

@app.route('/')
def home_page():
    return """ Welcome to my Film API!  
    Please use the READEME.md file in this project to know how to interact with me :)
    Thank you!"""

#browse films
@app.route('/browse/films', methods=['GET'])
# returns list of films
def browse_films():
    films = get_all_films()
    if films is None:
        return jsonify({"Error" : "Could not retrieve films"}), 500 #server error
    return jsonify(films), 200 #success
    
#to find a specific film with its ID
@app.route('/browse/films/<int:film_id>', methods=['GET'])
def find_film(film_id):
    film = get_film_by_id(film_id)
    if film is None: #i.e. film_id doesn't exist in database therefore client error 404
        return jsonify({"Error": "Film not found"}), 404
    return jsonify(film), 200

#adding a film!
@app.route('/add/film', methods=['POST'])
def add_film():
    data = request.json    
    success = insert_film(data['title'],
                data['release_year'],
                data['genre'],
                data['director'],
                data['IMDB_rating'],
                data['runtime'], 
                data['age_rating']) #my function returns true or false depending on if films were inserted
    if not success[0]:
        return jsonify({"Error": "Could not add film"}), 500
    
    return jsonify({"Message": "Film added successfully", "Film ID": success[1] }), 201

@app.route('/surprise', methods=['GET'])
def surprise_me_function(): #for if the user wants a random film to watch
    genre = request.args.get('genre') #looks in URL for parameter genre and takes its value
    choice = surprise_me(genre)
    if choice is None:
        return jsonify({"Error": "No title found with that genre"}), 404
    return jsonify(choice), 200

if __name__ == "__main__":
    app.run(debug=True)