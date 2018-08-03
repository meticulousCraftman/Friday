"""
Handles which module will serve the incoming command
USUAGE:
    from service_handler import serve
    serve(text_command)
"""

import re
from logger import logging
import telepot

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


def serve(msg, context):
    command = msg['text']

    for pattern, module in SERVICES:
        match = re.match(pattern, command)

        if pattern == command:
            logging.info(f'Service {module.NAME} found')
            module.serve(command, CONTEXT)

        elif match:
            logging.info(f'Service {module.NAME} found')
            result = match.group(1)
            module.serve(result, context)

        break
    
    # For loop else clause
    else:   
        logging.info(f'No service found that completes the request')
        content_type, chat_type, chat_id = telepot.glance(msg)
        CONTEXT['TelegramBot'].sendMessage(chat_id, 'No command found that caters your need.')
