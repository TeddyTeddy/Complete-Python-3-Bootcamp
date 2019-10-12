import card
from deck import Deck


def get_bet(chips):
    while True:
        bet = int(input(f'What is your bet in chips? (max. bet is {chips} chips): '))
        if bet <= chips:
            return bet
        else:
            print(f'You cannot bet more than {chips} chips. Asking again.. ')


def show_cards(hand, text, hide_first_card):
    print(text)
    for card in hand:
        if hide_first_card and hand.index(card) == 0:
            pass  # do not show the first card
        else:
            print(card, f'** Card Value: {card.value}')
    print('')


def ask_player_hit_or_stay():
    player_answer = input('Hit or stay? (h/s)').lower()
    while not (player_answer == 'h' or player_answer == 's'):
        player_answer = input('Hit or stay? (h/s)').lower()
    return player_answer


def hit(hand, new_cards):
    for card in new_cards:
        hand.append(card)


def do_get_1_or_11(card):
    question = f"For the', {card}, 'What should be the value? (1/11)?"
    answer = int(input(question))
    while answer != 1 and answer != 11:
        answer = int(input(question))
    return answer


def get_hand_value(hand):
    hand_value = 0
    for card in hand:
        hand_value += card.value
    return hand_value


def is_player_busted(player_hand):
    # check if there are aces that do not have any value (i.e. either 1 or 11)
    for card in player_hand:
        if card.rank == 'Ace' and card.value == -1:  # if card value is -1 for 'Ace', it value is not set yet!
            card.set_ace_value(do_get_1_or_11(card))

    # calculate the total value of the hand
    hand_value = get_hand_value(player_hand)

    # check if the player is busted
    return hand_value >= 21


def do_decide_aces_values(dealer_hand):
    # find ace card(s) (with a value -1) indexes, if any ace card is present in the dealer_hand
    np_aces_indexes = []   # np: non-processed
    for card in dealer_hand:
        if card.rank == 'Ace' and card.value == -1:
            np_aces_indexes.append(dealer_hand.index(card))

    # find the total of the dealer_hand excluding Aces with value=-1
    total_except_non_valued_aces = 0
    for card in dealer_hand:
        if card.value != -1:
            total_except_non_valued_aces += card.value

    for np_ace_index in np_aces_indexes:
        if total_except_non_valued_aces + 11 < 21:
            dealer_hand[np_ace_index].set_ace_value(11)
        else:
            dealer_hand[np_ace_index].set_ace_value(1)


def determine_winner(dealer_hand, player_hand):
    dealer_hand_value = get_hand_value(dealer_hand)
    player_hand_value = get_hand_value(player_hand)

    winner = None
    if dealer_hand_value >= 21:
        winner = 'Player'
    elif player_hand_value >= 21:
        winner = 'Dealer'
    elif dealer_hand_value == player_hand_value:
        winner = 'Tie'
    elif dealer_hand_value > player_hand_value:
        winner = 'Dealer'
    elif dealer_hand_value < player_hand_value:
        winner = 'Player'
    return winner


def do_play_dealers_hand(dealer_hand, deck):
    """
    The dealer will always Hit until the Dealer's value meets or exceeds 17
    :param dealer_hand : the hand (a list) to be modified
    :param deck: the deck of cards
    """
    # first, decide about Ace(s). If they should be either 1 or 11
    do_decide_aces_values(dealer_hand)  # modifies dealer_hand's card object if Ace(s)

    while get_hand_value(dealer_hand) < 17:
        hit(dealer_hand, deck.deal(num_of_cards=1))
        do_decide_aces_values(dealer_hand)  # modifies dealer_hand's card object if Ace(s)


def do_play_black_jack(chips):
    winner = None

    # Create a deck of 52 cards
    deck = Deck()
    # Shuffle the deck
    deck.shuffle()
    # Ask the Player for their bet
    # Make sure that the Player's bet does not exceed their available chips
    bet = get_bet(chips)
    # Deal two cards to the Dealer and two cards to the Player
    dealer_hand = deck.deal(num_of_cards=2)
    player_hand = deck.deal(num_of_cards=2)

    # Show only one of the Dealer's cards, the other remains hidden
    show_cards(dealer_hand, 'Dealer hand is:', hide_first_card=True)
    # Show both of the Player's cards
    show_cards(player_hand, 'Player hand is:', hide_first_card=False)

    while not is_player_busted(player_hand):
        # If the Player's hand doesn't Bust (go equal or over 21), ask if they'd like to Hit again.
        # Ask the Player, if he wishes to hit or stay
        player_wants_to = ask_player_hit_or_stay()
        if player_wants_to == 'h':
            hit(player_hand, deck.deal(num_of_cards=1))
            show_cards(player_hand, 'Player hand is:', hide_first_card=False)
            continue
        else:
            print('Player decided to stay. It is dealers turn now..')
            break
    else: # when while loop is over
        if is_player_busted(player_hand):
            winner = 'Dealer'

    if winner is None:  # winner is not clear yet and player stays at this point now
        # If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value
        # meets or exceeds 17
        do_play_dealers_hand(dealer_hand, deck)

    # Determine the winner
    winner = determine_winner(dealer_hand, player_hand)
    # Show only one of the Dealer's cards, the other remains hidden
    show_cards(dealer_hand, 'Dealer hand is:', hide_first_card=False)
    # Show both of the Player's cards
    show_cards(player_hand, 'Player hand is:', hide_first_card=False)

    # adjust the Player's chips according to the winner
    if winner is 'Dealer':
        print('Winner is dealer')
        chips -= bet
    elif winner is 'Player':  # winner is the player
        print('Winner is player')
        chips += bet
    else:
        print('There is a tie!')

    return chips


if __name__ == '__main__':
    chips = 10
    play_again = True
    while play_again:
        chips = do_play_black_jack(chips)
        if chips > 0:
            # Ask the Player if they'd like to play again
            play_again = input('Play again (y/n):').lower() == 'y'
        else:
            play_again = False
            print('Ran out of chips. Cannot play anymore. Get more chips!')
    print(f'At the end of black jack session, you have {chips} chips')
