import urllib.request
import json


#TMDB Api Key
API_KEY = "c37b1d1c084969689e9b52d21244dbeb"


def get_movie_id(search):
    """This gets the id from a search query on all movies in The Movie Data Base
    API.

    Args:
        search (str): Title of movie.

    Returns:
        int: Movie ID for first search result found.
    """
    formatted_search = search.replace(" ", "%20")
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + API_KEY + "&query=" + formatted_search

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data['results'][0]['id']


def get_original_title(movie_name):
    """This finds the exact title of the movie and returns the movie title
    from movie name.

    Args:
        movie_name (str): Title of movie.

    Returns:
        str: Movie exact title.
    """
    movie_id = get_movie_id(movie_name)
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + API_KEY

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())

    return data["original_title"]


def get_overview(movie_name):
    """This finds the overview of the movie from the title.

    Args:
        movie_name (str): Title of movie.

    Returns:
        str: Movie Overview.
    """
    movie_id = get_movie_id(movie_name)
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + API_KEY

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())

    return data["overview"]


def get_poster_img(movie_name):
    """This finds the exact path of the movie poster.

    Args:
        movie_name (str): Title of movie.

    Returns:
        str: Movie poster image url.
    """
    movie_id = get_movie_id(movie_name)
    url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + API_KEY

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())

    return "http://image.tmdb.org/t/p/w300/" + data["poster_path"]
