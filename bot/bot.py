import telegram
import configparser
import logging

class Chatbot:
    """
    The chatbot per se! Yay <3
    """
    def __init__(self, configfile):
        config = configparser.ConfigParser()
        config.read_file(configfile)
        self.bot = telegram.Bot(config['DEFAULT']['token'])

    def verify_bot(self):
        print(self.bot.get_me())
        return(self.bot.get_me().username, self.bot.get_me().id)

    def make_log():
        logging.basicConfig(\
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',\
                 level=logging.INFO)
