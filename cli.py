"""
Talk to Friday using command line interface
"""

from service_handler import serve

print("<==== Friday CLI ====>")
CONTEXT = {"iteration":1}
while True:
    if CONTEXT['iteration'] == 1:
        print("[*] Hello !!!")

    msg = input("<*> ")
    serve(msg, CONTEXT)
    CONTEXT['iteration'] += 1
