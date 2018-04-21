import subprocess
import os

from logger import *
from components.notifier import notify

NAME = "Downloader"


def serve(link, CONTEXT):
    os.chdir('/home/flash/Downloads')
    link = str(link)
    link = link.split(" ")
    link = "".join(link)
    logging.info(f'Downloading from the link : {link}')
    subprocess.call(['wget', f'{link}'])
    notify("Download has been started.")