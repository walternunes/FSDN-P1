import media
import csv
import fresh_tomatoes
from tmdb3 import set_key, searchMovie, set_cache, Movie, set_locale

# Config variables - Add your own API Key at API_KEY variable
API_KEY = ''
API_LOCALE = 'en'
CSV_FILE = 'data/movie_data.csv'

FAVORITE_MOVIES = [49026, 293660, 9741, 745, 153518, 603]


def fetch_api_data():
    """ fetch movie data from TMDB API and returns a list of Movie objects """
    # Set pre API configuration
    set_key(API_KEY)
    set_cache('null')
    set_locale(API_LOCALE)

    # Fetch movie data
    movieList = []
    for movie in FAVORITE_MOVIES:
        api_data = Movie(movie)
        api_poster = api_data.poster.geturl() + '?' + API_KEY
        movieList.append(media.Movie(api_data.title,
                                     api_data.overview,
                                     api_poster,
                                     api_data.youtube_trailers[0].geturl()))
    return movieList


def fetch_local_data():
    """ get movie data from a CSV file and returns a list of Movie objects """
    movieList = []
    with open(CSV_FILE, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for element in reader:
            movieList.append(media.Movie(element['Title'],
                                         element['Storyline'],
                                         element['Poster'],
                                         element['Trailer']))
    return movieList

if (API_KEY == ''):
    print('API TMDB Key not found: Fetching Data from CSV File')
    movies = fetch_local_data()
else:
    print('API TMDB Key found: Fetching Data from TMDB API')
    movies = fetch_api_data()

fresh_tomatoes.open_movies_page(movies)
