import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'Card: suit: {self.suit} rank: {self.rank} (value: {values[self.rank]})'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.deck.append(new_card)

    def __str__(self):
        result = 'The deck is:\n'
        for card in self.deck:
            result += f'{card}\n'
        return result

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        """Deals one card at a time"""
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of non-processed aces

    def add_card(self, card):
        if card.rank == 'Ace':
            self.aces += 1
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value >= 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.chips = 100
        self.bet = 0

    def win_bet(self):
        self.chips += self.bet

    def lose_bet(self):
        self.chips -= self.bet


if __name__ == '__main__':
    test_deck = Deck()
    print(test_deck)
    print('\nDeck is shuffled:')
    test_deck.shuffle()
    print(test_deck)
