"""
Handles which module will serve the incoming command
USUAGE:
    from service_handler import serve
    serve(text_command)
"""

import re
from logger import *

from services import notification
from services import downloader
from services import speak


SERVICES = [
    [r'notify (.*)', notification],
    [r'download (.*)', downloader],
    [r'speak (.*)', speak],
]


def serve(command, CONTEXT):
    for pattern, module in SERVICES:
        match = re.match(pattern, command)
        if match:
            logging.info(f'Service {module.NAME} found')
            result = match.group(1)
            module.serve(result, CONTEXT)
        else:
            logging.info(f'Service {module.NAME} does not serve this command.')
