import sys
import pprint
import telegram
from telegram.ext import (Updater, CommandHandler)
from mongoengine import *
from pymongo import *
import config
import logging

from food.Food import Food

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("__main__")
admin = []
chat_id = []
# foods = connect(config.DB_COLL, host=config.DB_HOST, port=config.DB_PORT)
db = MongoClient(host=config.DB_HOST, port=config.DB_PORT)


def start(bot, update):
    update.message.reply_text('Hello!')


def help(bot, update):
    update.message.reply_text('Help!')


def random(bot, update):
    with MongoClient(config.DB_HOST, config.DB_PORT) as client:
        db = client[config.DB_COLL]
        wfoods = db.ieat.foods
        for s in wfoods.find():
            pprint.pprint(s)
            print("random")
            update.message.reply_text("random")
            update.message.reply_text(str(s))
            # sample = Food.objects(group='Dairy and Egg Products')
            # for s in sample:
            #     pprint.pprint(s)
            #     print("random")
            #     update.message.reply_text("random")
            #     update.message.reply_text(str(s))


def error(bot, update, error_msg):
    log.warning('Update "%s" caused error "%s"' % (update, error_msg))


def main(token):
    updater = Updater(token=token)
    d = updater.dispatcher

    d.add_handler(CommandHandler(config.CMD_START, start))
    d.add_handler(CommandHandler(config.CMD_HELP, help))
    d.add_handler(CommandHandler(config.CMD_RANDOM, random))

    d.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main(sys.argv[1])
