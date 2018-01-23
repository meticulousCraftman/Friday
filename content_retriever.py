"""
Makes sense of commands and calls the appropriate api endpoint of the content retrieval service
The content it returns must be fit to use as a search query on search engines (E.g. The pirate Bay)

By default, it uses The Movie Database's api to call to get movies/TV Shows,
"""
import tmdbsimple as tmdb
from logger import *
import maya

tmdb.API_KEY = '9c5b5cbae99ec6c5713b88fe8f829a2f'
movies = tmdb.movies.Movies()
tv = tmdb.tv.TV()


def _get_popular_movies():
    logging.debug('Getting popular movies')
    for movie in movies.popular()['results']:
        yield {
            'title': movie['title'],
            'year': maya.parse(movie['release_date']).year,
            'type': 'movies',
        }


def _get_latest_movies():
    logging.debug('Getting latest movies')
    for movie in movies.latest()['results']:
        yield {
            'title': movie['title'],
            'year': maya.parse(movie['release_date']).year,
            'type': 'movies',
        }


content = {
    'popular movies': _get_popular_movies().__next__,
    'popular movie': _get_popular_movies().__next__,
    'latest movie': _get_latest_movies().__next__,
    'latest movies': _get_latest_movies().__next__,
}


# API
def get_content(cmd):
    """
    Args:
        cmd: the command to execute
        This function is supposed to block until content is found

    Returns:
        The content as a `dict`

        keys:
            title: the title of content (E.g. Movie name)
            year:  the year that content was released
            type: movie / tv show / xxx
    """
    return content[cmd]()
