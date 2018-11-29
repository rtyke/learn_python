from datetime import datetime
import logging
import os

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


HTTP_API = os.environ['TOKEN']
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
}

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)


CURRENT_YEAR = datetime.strftime(datetime.now(), '%Y')


def greet_user(bot, update):
    text = '/start invoked'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(f'user said: {user_text}')
    update.message.reply_text(f'bot responsed: {user_text}')


def get_constellation(bot, update):
    planet = update.message.text.split()[1].lower().capitalize()
    planet_obj = getattr(ephem, planet, None)
    if planet_obj:
        constellation = ephem.constellation(planet_obj(CURRENT_YEAR))
        update.message.reply_text(constellation[1])
    else:
        update.message.reply_text(f'{planet} is not a planet')


def main():
    mybot = Updater(HTTP_API, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
