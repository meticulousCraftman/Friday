"""Retrieves the media download url from internet or wherever
pip install git+https://github.com/mwalercz/TPB.git@fix-403-forbidden
"""
import requests
from tpb import TPB
from tpb import CATEGORIES, ORDERS
from logger import *


def _get_fastest_proxy():
    return 'https://' + requests.get('https://thepiratebay-proxylist.org/api/v1/proxies').json()['proxies'][0]['domain']


t = TPB('https://thepiratebay.org/')
logging.info(f'Using proxy - {t.base_url}')

category_map = {
    'movies': (CATEGORIES.VIDEO.ALL)
}


def _get_best_torrent(query):
    search = t.search(f'{query["title"]} {query["year"]}', category=category_map[query['type']])
    return next(search.items()).magnet_link


# API
def get_download_url(query):
    """
    Gets the download url from a content provider, like TPB
    This function is supposed to block until a command can be issued

    Args:
        query: Search query for search engines

    Returns:
        magnet URL / download link.
        (Should be  compatible with the downloader in place)
    """
    return _get_best_torrent(query)
