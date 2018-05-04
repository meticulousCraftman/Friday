"""
Gets the command from wherever.
Default is to get a command via IFTTT, (triggered by google assistant and forwarded to telegram)
Usage:
    from commander import get_command
    command = get_command()
"""
import datetime
import time
from telethon import TelegramClient
from logger import logging

# Create a Telegram Application and paste the
# APP_ID and API_HASH here
APP_ID = 266606
API_HASH = '3a0c50e76246f51e414f1e3a7c5fad53'


class IFTTTClient:
    def __init__(self, api_id=APP_ID, api_hash=API_HASH):
        # self.latest_msg_date = maya.now()
        self.CONTEXT = {}
        self.latest_msg_date = datetime.datetime.now()
        logging.debug(f'set latest msg date to - {self.latest_msg_date}')

        logging.info('starting telegram client')
        self.client = TelegramClient('session_id', api_id, api_hash)
        self.CONTEXT['telegramClient'] = self.client
        self.client.start()
        self.latest_msg = self.client.get_messages('IFTTT')[0].message

    def get_latest_command(self):
        logging.debug('getting message history')
        msg = self.client.get_messages('IFTTT')[0]

        if self.latest_msg != msg.message:
            logging.debug(f'new msg found - {repr(msg.message)}')

            self.latest_msg = msg.message
            logging.debug('set latest msg date to -')

            return (msg.message, self.CONTEXT,)
        
        logging.debug('no new msg found')
        return ("", {})


client = IFTTTClient()


# API
def get_command():
    """
    Get a command from some source (E.g. IFTTT)
    This function is supposed to block until a command can be issued
    """
    while True:
        cmd, CONTEXT = client.get_latest_command()
        if cmd:
            return (cmd, CONTEXT)
        
        time.sleep(1)
        return ("", {})date