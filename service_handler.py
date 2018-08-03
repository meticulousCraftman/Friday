import re

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
    command = msg

    for pattern, module in SERVICES:
        match = re.match(pattern, command)

        if pattern == command:
            module.serve(command, context)

        elif match:
            result = match.group(1)
            module.serve(result, context)

        break
    
    # For loop else clause
    else:
        print("[*] No matching command found.")
