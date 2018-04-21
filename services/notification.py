from components.notifier import notify

NAME = "Notification"


def serve(command, CONTEXT):
    notify(command)