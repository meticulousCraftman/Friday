"""
Handles which module will serve the incoming command
USUAGE:
    from service_handler import serve
    serve(text_command)
"""

import re
from logger import logging
import settings

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

        if pattern == command:
            logging.info(f'Service {module.NAME} found')
            module.serve(command, CONTEXT)

        elif match:
            logging.info(f'Service {module.NAME} found')
            result = match.group(1)
            module.serve(result, CONTEXT)

        break
    
    # For loop else clause
    else:   
        logging.info(f'No service found that completes the request')
        CONTEXT['telegramClient'].send_message(settings.REPLY_TELEGRAM_USERNAME, 'Unable to find a service that fulfills that request.')
