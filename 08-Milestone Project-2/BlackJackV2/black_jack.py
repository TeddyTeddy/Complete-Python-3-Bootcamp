from hand import PlayerHand
from hand import DealerHand
from deck import Deck


def get_bet(chips):
    while True:
        try:
            bet = int(input(f'What is your bet in chips? (min. bet is 1 and max. bet is {chips} chips): '))
        except ValueError:
            print('Please enter a number. Asking again..')
            continue
        else:  # user entered a number
            if 1 <= bet <= chips:
                return bet
            else:
                print(f'Wrong number. Min bet is 1 and max bet is {chips} chips). Asking again.. ')


def ask_player_hit_or_stay():
    player_answer = input('Hit or stay? (h/s)').lower()
    while not (player_answer == 'h' or player_answer == 's'):
        player_answer = input('Hit or stay? (h/s)').lower()
    return player_answer


def determine_winner(dealer_hand, player_hand):
    dealer_hand_value = dealer_hand.value()
    player_hand_value = player_hand.value()

    winner = None
    if dealer_hand.is_busted():
        winner = 'Player'
    elif player_hand.is_busted():
        winner = 'Dealer'
    elif dealer_hand_value == player_hand_value:
        winner = 'Tie'
    elif dealer_hand_value > player_hand_value:
        winner = 'Dealer'
    elif dealer_hand_value < player_hand_value:
        winner = 'Player'
    return winner


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
    dealer_hand = DealerHand(deck)
    player_hand = PlayerHand(deck)

    # Show only one of the Dealer's cards, the other remains hidden
    dealer_hand.show_cards(hide_first_card=True)
    # Show both of the Player's cards
    player_hand.show_cards()

    while not player_hand.is_busted():
        # If the Player's hand doesn't Bust (go equal or over 21), ask if they'd like to Hit again.
        # Ask the Player, if he wishes to hit or stay
        player_wants_to = ask_player_hit_or_stay()
        if player_wants_to == 'h':
            player_hand.hit(deck, num_of_cards=1)
            player_hand.show_cards()
            continue
        else:
            print('Player decided to stay. It is dealers turn now..')
            break

    if not player_hand.is_busted():  # winner is not clear yet and player stays at this point now
        # If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value
        # meets or exceeds 17
        dealer_hand.do_play_dealers_hand(deck)

    # Determine the winner
    winner = determine_winner(dealer_hand, player_hand)
    # Show only one of the Dealer's cards, the other remains hidden
    dealer_hand.show_cards()
    # Show both of the Player's cards
    player_hand.show_cards()

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
