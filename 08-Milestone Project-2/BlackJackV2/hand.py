from abc import ABCMeta, abstractmethod
import card
import deck


class Hand:
    __metaclass__ = ABCMeta

    def __init__(self, deck):
        self._cards = []
        new_cards = deck.deal(num_of_cards=2)
        for card in new_cards:
            self._cards.append(card)
        self.owner = None

    def hit(self, deck, num_of_cards):
        new_cards = deck.deal(num_of_cards=num_of_cards)
        for card in new_cards:
            self._cards.append(card)

    def show_cards(self, hide_first_card=False):
        print(f"The {self.owner}'s hand is:")
        for card in self._cards:
            if hide_first_card and self._cards.index(card) == 0:
                pass  # do not show the first card
            else:
                print(card, f'** Card Value: {card.value}')
        print('')

    def is_busted(self):
        value = self.value()
        return value >= 21

    @abstractmethod
    def value(self):
        pass


class PlayerHand(Hand):

    def __init__(self, deck):
        super().__init__(deck)
        self.owner = 'Player'

    @staticmethod
    def _do_get_1_or_11(card):
        question = f"For the {card}, What should be the value? (1/11)?"
        answer = int(input(question))
        while answer != 1 and answer != 11:
            answer = int(input(question))
        return answer

    def value(self):
        # handle all non-handled Ace cards first
        for card in self._cards:
            if card.rank == 'Ace' and card.value == -1:  # if we have an Ace that is not settled yet
                ace_value = PlayerHand._do_get_1_or_11(card)
                card.set_ace_value(ace_value)
        hand_value = 0
        for card in self._cards:
            hand_value += card.value
        return hand_value


class DealerHand(Hand):

    def __init__(self, deck):
        super().__init__(deck)
        self.owner = 'Dealer'

    def _do_decide_aces_values(self):
        # find ace card(s) (with a value -1) indexes, if any ace card is present in the dealer_hand
        np_aces_indexes = []  # np: non-processed
        for card in self._cards:
            if card.rank == 'Ace' and card.value == -1:  # if non-processed card comes in
                np_aces_indexes.append(self._cards.index(card))

        # find the total of the dealer_hand excluding Aces with value=-1
        total_except_non_valued_aces = 0
        for card in self._cards:
            if card.value != -1:
                total_except_non_valued_aces += card.value

        for np_ace_index in np_aces_indexes:
            if total_except_non_valued_aces + 11 < 21:
                self._cards[np_ace_index].set_ace_value(11)
            else:
                self._cards[np_ace_index].set_ace_value(1)

    def value(self):
        self._do_decide_aces_values()
        hand_value = 0
        for card in self._cards:
            hand_value += card.value
        return hand_value

    def do_play_dealers_hand(self, deck):
        """
        The dealer will always Hit until the Dealer's value meets or exceeds 17
        :param self : the dealer's hand to be modified
        :param deck: the deck of cards
        """
        while self.value() < 17:
            self.hit(deck, num_of_cards=1)
