import webbrowser

"""This module contains the Class Movie. Movie holds the object responsible
for storing movie data. To take advantage of this class, import this file. """

class Movie ():
    """This class provides a way to store movie reltated information."""

    VALID_RATINGS=["G", "PG", "PG-13", "R"]
    #Constructor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """This is the constructor for the Movie class

        Args:
            movie_title (str): Title of the movie.
            movie_storyline (str): Short storyline of the movie.
            poster_image (str): URL to image of movie's poster.
            trailer_youtube (str): URL to Youtube trailer of movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #Function shows trailer in new browser window
    def show_trailer(self):
        """show_trailer() opens the movie trailer in a browser window.

        Returns:
            Void

        """
        webbrowser.open(self.trailer_youtube_url)
