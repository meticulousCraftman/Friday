"""
Inits the python logging module with suitable config when imported.
Nothing fancy, just avoids repeating yourself when ALL YOU WANNA DO IS LOG!

USAGE:
    from logger import *

    logging.debug(<msg>)
    logging.info(<msg>)
"""

import logging

log_format = '[%(asctime)s] [%(name)s] [%(levelname)s] -> %(message)s'
date_format = '%m/%d/%y %I:%M:%S %p'

# log every little detail to file
logging.basicConfig(
    filename='telegram_bot.log',
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    filemode='w'
)

# log only the INFO level stuff to stdout
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(log_format, date_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
