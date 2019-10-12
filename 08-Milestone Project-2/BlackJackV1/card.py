suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
ranks_and_values = {'Ace': -1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                    'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = ranks_and_values[self.rank]  # if 'Ace' then initialized temporarily to -1

    def __str__(self):
        return f'Card: suit = {self.suit}, rank = {self.rank}'

    def set_ace_value(self, value):
        if self.rank is not 'Ace':
            raise AssertionError  # cannot set any card other than Ace a value 1 or 11
        if value != 1 and value != 11:
            raise AssertionError  # cannot set a value other than 1 or 11
        self.value = value
