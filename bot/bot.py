import telegram
import os
from telegram.ext import Updater
from configparser import ConfigParser
import logging

def retrieve_token():
    config = ConfigParser()
    config.read_file(open(str(os.getcwd())+'/bot/config.ini'))
    return(config['DEFAULT']['token'])

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

    def verify_bot(self):
        # print(self.bot.get_me())
        return(self.bot.get_me().username, self.bot.get_me().id)

    def make_log(self):
        print(self.bot.getLogger())

    # def run(self):
    #     pass

if __name__ == '__main__':
    token = retrieve_token()
    x = Chatbot(token)
