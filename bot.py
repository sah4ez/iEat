import sys
import telegram
from telegram.ext import (Updater, CommandHandler)
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("__main__")
admin = []
chat_id = []


def start(bot, update):
    update.message.reply_text('Hello!')


def help(bot, update):
    update.message.reply_text('Help!')


def error(bot, update, error_msg):
    log.warning('Update "%s" caused error "%s"' % (update, error_msg))


def main(token):
    updater = Updater(token=token)
    d = updater.dispatcher

    d.add_handler(CommandHandler('start', start))
    d.add_handler(CommandHandler('help', help))

    d.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main(sys.argv[1])
