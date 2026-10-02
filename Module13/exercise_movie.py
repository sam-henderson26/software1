import json

movie = {
    "Title": "Resident Evil",
    "Year": "2026",
    "Actors": "Austin Abrams"
}

# with open("Module13/movie.json", "w") as file:
    # json.dump(movie, file)

# Code above creates a file with the information about the movie, by "dumping" the json file into it

with open("Module13/movie.json", "r") as file:
    movie_data = json.load(file)
    print(movie_data)

# Then (code above) loads the data from the file and saves it as "movie_data" and then prints all of it;
# if only some of the information is required, then see the json_example.py file.
