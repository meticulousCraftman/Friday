import subprocess
import os

from .notification import notify

NAME = "Downloader"


def serve(link, context):
    os.chdir('/home/flash/Downloads')
    link = str(link)
    link = link.split(" ")
    link = "".join(link)
    subprocess.call(['wget', f'{link}'])
    notify("Download has been started.")