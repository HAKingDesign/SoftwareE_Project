from unittest import mock
from unittest.mock import patch
from unittest import TestCase
import unittest
import Blackjack_final

class testBlackJack(TestCase):

    @patch('Blackjack_final.getBet', return_value = 'zxcrgghfd456')
    def test1(self, input):
        self.assertRaises(ValueError, Blackjack_final.playGame)

    @patch('Blackjack_final.getChoice', return_value = 'hgf456456gf')
    def test2(self, input):
        self.assertRaises(ValueError, Blackjack_final.playGame)
    

unittest.main()
