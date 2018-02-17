import unittest
import os
from bot.bot import Chatbot

class TestBot(unittest.TestCase):

    def setUp(self):
        self.bot = Chatbot(open(str(os.getcwd())+'/bot/config.ini'))

    def test_nothing(self):
        """
        Check if testing is really ocurring
        """
        pass

    def test_if_bot_is_unbchatbot(self):
        """
        Check if bot being initialized is trully the unbchatbot
        """
        self.assertEqual(self.bot.verify_bot(), ('unbchatbot', 330147863))

    def test_if_bot_logging_works(self):
        """
        Check for bot logging
        """
        pass

if __name__ == '__main__':
    unittest.main()
