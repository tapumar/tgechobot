import telegram
import os
import sys
from telegram.ext import Updater, CommandHandler
from configparser import ConfigParser
import logging

def retrieve_token():
    try:
        config = ConfigParser()
        config.read_file(open(str(os.getcwd())+'/bot/config.ini'))
        return(config['DEFAULT']['token'])
    except:
        return(-1)


class Chatbot:
    """
    The chatbot per se! Yay <3
    """
    def __init__(self, token):
        logging.basicConfig(\
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
                 level=logging.INFO)
        self.bot = telegram.Bot(token)
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

    def verify_bot(self):
        # print(self.bot.get_me())
        return(self.bot.get_me().username, self.bot.get_me().id)

    def make_log(self):
        print(self.bot.getLogger())

    def start(self, bot, update):
        """
        The variables bot and update are respectively
        the bot info and the user info.
        """
        start_text = "This is the bot!"
        bot.send_message(chat_id=update.message.chat_id, text=start_text)

    def run(self):
        self.updater.start_polling()

    def stop(self):
        self.updater.stop()

if __name__ == '__main__':
    token = retrieve_token()
    if(token == -1):
        print('Configuration file not found.')
        sys.exit(1)
    x = Chatbot(token)
    x.run()
    print("Running")
