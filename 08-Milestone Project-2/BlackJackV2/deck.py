import card
import random


class Deck:
    def __init__(self):
        self.__cards = []
        for suit in card.suits:
            for rank in card.ranks:
                new_card = card.Card(suit, rank)
                self.__cards.append(new_card)

    @staticmethod
    def _get_shuffle_index(card_index):
        while True:
            shuffle_index = random.randint(0, 51)
            if shuffle_index != card_index:
                return shuffle_index

    def shuffle(self):
        for card_one_index in range(0, 52):  # between 0 to 51 inclusive
            card_two_index = Deck._get_shuffle_index(card_one_index)
            card_one = self.__cards[card_one_index]  # hold card_one reference
            card_two = self.__cards[card_two_index]  # hold card_two reference
            self.__cards.remove(card_one)
            self.__cards.remove(card_two)
            self.__cards.insert(card_one_index, card_two)
            self.__cards.insert(card_two_index, card_one)

    def deal(self, num_of_cards):
        if num_of_cards <= 0:
            raise AssertionError  # num_of_cards cannot be negative or zero
        result = []
        while num_of_cards > 0:
            result.append(self.__cards.pop())  # deal a card into result list, can raise IndexError if deck is empty
            num_of_cards -= 1
        return result

    def _print(self):
        print('The deck is:')
        for card in self.__cards:
            print(card)




