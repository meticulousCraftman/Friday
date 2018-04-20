"""
Handles which module will serve the incoming command
USUAGE:
    from service_handler import serve
    serve(text_command)
"""

import re
from logger import *

from services import notification


SERVICES = [
    [r'notify (.*)', notification.serve]
]


def serve(command, CONTEXT):
    for pattern, action in SERVICES:
        match = re.match(pattern, command)
        if match:
            logging.info(f'Found a service for the command: {command}')
            result = match.group(1)
            action(result, CONTEXT)
        else:
            logging.info('No service found for the given command')