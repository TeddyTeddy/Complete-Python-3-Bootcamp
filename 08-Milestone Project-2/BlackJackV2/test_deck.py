import unittest
from deck import Deck


class TestDeck(unittest.TestCase):
    def test_shuffle(self):
        deck = Deck()
        print('Before shuffle, the deck is')
        deck._print()
        deck.shuffle()
        print('After shuffle, the deck is')
        deck._print()


if __name__ == '__main__':
    unittest.main()
