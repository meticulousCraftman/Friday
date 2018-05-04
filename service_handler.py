"""
Handles which module will serve the incoming command
USUAGE:
    from service_handler import serve
    serve(text_command)
"""

import re
from logger import logging

from services import notification
from services import downloader
from services import speak
from services import shutdown


SERVICES = [
    [r'notify (.*)', notification],
    [r'download (.*)', downloader],
    [r'speak (.*)', speak],

    [r'shutdown my laptop', shutdown],
    [r'shutdown my computer', shutdown],
    [r'shutdown my pc', shutdown],
    
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
