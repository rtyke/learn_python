from datetime import datetime
import logging
import os
import sys

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


HTTP_API = os.environ['TOKEN']
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
}

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG,
    filename='bot.log',
)
# logging.StreamHandler(sys.stdout)

CURRENT_YEAR = datetime.strftime(datetime.now(), '%Y')


def count_words(bot, update):
    words_to_count = update.message.text.replace('/wordcount', '')
    if not words_to_count:
        update.message.reply_text('Please type one or several words after /wordcount')
    else:
        words_number = len(words_to_count.split())
        update.message.reply_text(f'You typed {words_number} words')
#     TODO check another cases


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


def get_next_fool_moon(bot, update):
    provided_date = update.message.text.replace('/next_fool_moon', '')
#   TODO check date format
    next_fool_moon = ephem.next_full_moon(provided_date)
    update.message.reply_text(f'The next fool moon is at {next_fool_moon}')



def main():
    mybot = Updater(HTTP_API, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(CommandHandler('wordcount', count_words))
    dp.add_handler(CommandHandler('next_fool_moon', get_next_fool_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
