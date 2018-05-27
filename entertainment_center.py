import media
import fresh_tomatoes
import tmdb_api

movie = ["harry potter", "gangs of new york", "lord of the rings"]


#Creating Harry Potter Instance of Movie
harry_potter= media.Movie(tmdb_api.get_original_title(movie[0]),
tmdb_api.get_overview(movie[0]),
tmdb_api.get_poster_img(movie[0]),
"https://www.youtube.com/watch?v=PbdM1db3JbY")

#Creating Gangs of New York Instance of Movie
gangs_of_NY = media.Movie(tmdb_api.get_original_title(movie[1]),
tmdb_api.get_overview(movie[1]),
tmdb_api.get_poster_img(movie[1]),
"https://www.youtube.com/watch?v=qHVUPri5tjA")

#Creating Lord of the Rings Instance of Movie
lord_of_the_rings = media.Movie(tmdb_api.get_original_title(movie[2]),
tmdb_api.get_overview(movie[2]),
tmdb_api.get_poster_img(movie[2]),
"https://www.youtube.com/watch?v=V75dMMIW2B4")

#Formating and sending data to fresh_tomatoes
created_movies =[harry_potter, lord_of_the_rings, gangs_of_NY]
fresh_tomatoes.open_movies_page(created_movies)

#print(tmdb_api.get_poster_img("harry potter"))
