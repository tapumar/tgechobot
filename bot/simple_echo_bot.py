import telegram
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from configparser import ConfigParser
import logging


def retrieve_token():
    try:
        config = ConfigParser()
        config.read_file(open(str(os.getcwd())+'/bot/config.ini'))
        return(config['DEFAULT']['token'])
    except e:
        return(e)


class Chatbot:
    """
    The chatbot per se!
    """
    def __init__(self, token):
        self.bot = telegram.Bot(token)

        # The Updater: Its purpose is to receive the updates
        # from Telegram and to deliver them to the dispatcher.
        self.updater = Updater(token=token)

        # The dispatcher sends all kinds of updates to its registered handlers.
        self.dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        echo_handler = MessageHandler(Filters.text, self.echo)
        self.dispatcher.add_handler(echo_handler)

    def verify_bot(self):
        # print(self.bot.get_me())
        return(self.bot.get_me().username, self.bot.get_me().id)

    def start(self, bot, update):
        """
        Start command to start bot on Telegram.
        @bot = information about the bot
        @update = the user info.
        """
        start_text = "This is the bot!"
        bot.send_message(chat_id=update.message.chat_id, text=start_text)

    def echo(self, bot, update):
        """Echo the user message."""
        # print(update)
        update.message.reply_text(update.message.text)

    def run(self):
        # Start the Bot
        self.updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()


if __name__ == '__main__':
    token = retrieve_token()
    if(not token):
        print('Configuration file not found.')
        sys.exit(1)
    x = Chatbot(token)
    x.run()
