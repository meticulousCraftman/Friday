# TODO make a system independent notification manager.

import subprocess

NAME = "Notification"


def notify(text):
    subprocess.call(['notify-send', f'"{text}"'])


def serve(command, context):
    notify(command)