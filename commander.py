"""
Gets the command from wherever.
Default is to get a command via IFTTT, (triggered by google assistant and forwarded to telegram)
Usage:
    from commander import get_command
    command = get_command()
"""
import maya
from telethon import TelegramClient

from logger import *


class IFTTTClient:
    def __init__(self, api_id=196708, api_hash='f0c865a3ecc24c4af25dfae27d475938'):
        self.latest_msg_date = maya.now()
        logging.debug(f'set latest msg date to - {self.latest_msg_date}')

        logging.info('starting telegram client')
        self.client = TelegramClient('session_name', api_id, api_hash)
        self.client.start()

    def get_latest_command(self):
        logging.debug('getting message history')
        msg = self.client.get_message_history('IFTTT')[0]
        date = maya.MayaDT.from_datetime(msg.date)
        if date > self.latest_msg_date:
            logging.debug(f'new msg found - {repr(msg.message)}')

            self.latest_msg_date = date
            logging.debug(f'set latest msg date to - {self.latest_msg_date}')

            return msg.message
        logging.debug('no new msg found')


client = IFTTTClient()


# API
def get_command():
    """
    Get a command from some source (E.g. IFTTT)
    This function is supposed to block until a command can be issued

    Returns:
        the command as `str`
    """
    while True:
        cmd = client.get_latest_command()
        if cmd:
            return cmd
        maya.time.sleep(1)