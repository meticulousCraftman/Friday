"""
Talk to Friday using command line interface
"""

from service_handler import serve

print("<==== Friday CLI ====>")

while True:
    CONTEXT = {}
    msg = input("<*> ")
    serve(msg, CONTEXT)