"""
Pop up notification on the desktop
for showing that a command was received

USUAGE:
	from notifier import notify
	notify("Notification text goes here")

"""

import subprocess

def notify(text):
	subprocess.call(['notify-send',f'"{text}"'])