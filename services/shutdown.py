import subprocess

ACTIVATION = [
    'shutdown my laptop',
    'shutdown my computer',
    'shutdown my pc',
]

NAME = "Shutdown"


def serve(command, context):
    # Shutdown the computer immediately
    subprocess.call(["shutdown", "-s", "-t", "0"])