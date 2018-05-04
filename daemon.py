"""
Working:
    Call commander's get_command and wait to command
    forward the command to content_retriever and get content name (E.g.: movie name)
    forward content name to content_provider to get media link
    forward media link to downloader
    repeat
"""
if __name__ == '__main__':
    from logger import logging
    from commander import get_command
    from service_handler import serve


    while True:
        try:
            cmd = get_command()
            cmd = cmd.strip()

            logging.info(f'Got command {repr(cmd)}')
            CONTEXT = {}
            serve(cmd, CONTEXT)


        except KeyboardInterrupt:
            logging.info('exiting!')
            break
