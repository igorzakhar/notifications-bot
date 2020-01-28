import logging
import os
import sys
import time

from dotenv import load_dotenv
import requests
import telegram

from log import create_logger_bot


def receive_notification(url, token, timestamp=''):
    headers = {'Authorization': f'Token {token}'}
    payload = {'timestamp': timestamp}

    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()


def run_bot(api_url, api_token, chat_id, bot_token, proxy, logger=None):
    reqproxy = None
    if proxy:
        reqproxy = telegram.utils.request.Request(proxy_url=proxy)

    bot = telegram.Bot(token=bot_token, request=reqproxy)

    timestamp = ''

    if logger:
        logger.warning('Бот запущен.')

    while True:
        try:
            notice = receive_notification(api_url, api_token, timestamp)

            timestamp = notice.get('timestamp_to_request', '')

            if notice.get('status') != 'found':
                continue

            for attempts in notice.get('new_attempts'):
                lesson_title = attempts.get('lesson_title')
                is_negative = attempts.get('is_negative')
                result = (
                    "Преподавателю все понравилось, "
                    "можно приступать к следующему уроку."
                )
                if is_negative:
                    result = "К сожалению, в работе нашлись ошибки."

                notification_msg = (
                    f'У вас проверили работу "{lesson_title}".\n\n{result}'
                )

                bot.send_message(chat_id=chat_id, text=notification_msg)

            timestamp = notice.get('last_attempt_timestamp', '')

        except Exception as err:
            if logger:
                logger.error('Бот упал с ошибкой.')
                logger.exception(err, exc_info=True)
            time.sleep(60)
            continue


def main():
    load_dotenv()
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    logging.getLogger('telegram').setLevel(logging.WARNING)

    api_url = os.getenv('DEVMAN_API_URL')
    api_token = os.getenv('DEVMAN_API_TOKEN')
    tg_token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    socks5_proxy = os.getenv("SOCKS5_PROXY")
    proxy_url = ''

    if socks5_proxy:
        proxy_url = f'socks5://{socks5_proxy}'

    logger = create_logger_bot(
        'notifications_bot',
        bot_token=tg_token,
        chat_id=chat_id
    )
    run_bot(api_url, api_token, chat_id, tg_token, proxy_url, logger=logger)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
