import logging

import telegram


class BotLogsHandler(logging.Handler):

    def __init__(self, bot_token, chat_id):
        super().__init__()
        self.bot_token = bot_token
        self.chat_id = chat_id
        self.bot = telegram.Bot(token=self.bot_token)

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


def create_logger_bot(logger_name, bot_token=None, chat_id=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    if bot_token and chat_id:
        logs_handler = BotLogsHandler(bot_token, chat_id)
        log_format = logging.Formatter('%(message)s')
        logs_handler.setFormatter(log_format)
        logger.addHandler(logs_handler)

    return logger
