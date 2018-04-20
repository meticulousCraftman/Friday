"""
Working:
    Call commander's get_command and wait to command
    forward the command to content_retriever and get content name (E.g.: movie name)
    forward content name to content_provider to get media link
    forward media link to downloader
    repeat
"""
if __name__ == '__main__':
    from logger import *
    from commander import get_command
    from service_handler import serve

    # from content_retriever import get_content
    # from content_provider import get_download_url
    # from downloader import start_download

    while True:
        try:
            cmd = get_command()
            cmd = cmd.strip()

            logging.info(f'Got command {repr(cmd)}')
            CONTEXT = {}
            serve(cmd, CONTEXT)

            # content = get_content(cmd)
            # logging.info(f'Got content {repr(content)}')
            #
            # magnet = get_download_url(content)
            # logging.info(f'Got download url {magnet}')
            #
            # start_download(magnet)
            # logging.info('Started download')
        except KeyboardInterrupt:
            logging.info('exiting!')
            break
