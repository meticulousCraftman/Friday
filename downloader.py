from logger import *
import subprocess


def _add_download_to_deluge(magnet):
    subprocess.call(['deluge-console', 'add', magnet])
    logging.debug('Added magnet to deluge')


def start_download(url):
    """
    Starts downloading the provided media url
    This function is supposed to be non-blocking
    url:
        the media url (magnet link for default config)
    Returns:
        None
    """
    return _add_download_to_deluge(url)
