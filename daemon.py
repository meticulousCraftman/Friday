"""
Working:
    Call commander's get_command and wait to command
    forward the command to content_retriever and get content name (E.g.: movie name)
    forward content name to content_provider to get media link
    forward media link to downloader
    repeat
"""
if __name__ == '__main__':
    import sys
    import time
    import settings
    import telepot
    from logger import logging
    from service_handler import serve

    CONTEXT = {}
    TelegramBot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)
    CONTEXT['TelegramBot'] = TelegramBot
 
 
    def handler(msg):
        text = msg['text']
        logging.info(f'Got command {repr(text)}')
        serve(msg, CONTEXT)
    try:
        TelegramBot.message_loop(handler)

        print('Listening....')
        
        # Keep the progarm running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Byeeeee')
        sys.exit(0)