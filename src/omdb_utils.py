# omdb_utils.py
import requests

def get_movie_details(title, api_key):

    url = f"http://www.omdbapi.com/?t={title}&plot=full&apikey={api_key}"
    res = requests.get(url).json()
    if res.get("Response") == "True":
        result = res.get("Plot", "N/A"), res.get("Poster", "N/A"), res.get("Runtime", "N/A"), res.get("Language", "N/A"), res.get("Released", "N/A"), res.get("imdbRating", "N/A")
        plot = result[0]
        poster = result[1]
        runtime = result[2]
        language = result[3]
        released = result[4]
        imdbRating = result[5]
        return plot, poster, runtime, language, released, imdbRating

    return "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"