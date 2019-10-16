from card import Card
from card import Deck
from card import Hand
from card import Chips

playing = True


def take_bet(chips):
    while True:
        try:
            question = f'Enter your bet (min. 1 chip, max. {chips.chips} chips): '
            bet = int(input(question))
        except ValueError:
            continue  # user entered a non-integer input
        else:         # user entered an integer input
            if 0 < bet <= chips.chips:
                chips.bet = bet
                break


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        answer = input('Do you want to hit or stay (h/s)?: ')
        if answer == 'h':
            hit(deck, hand)
        elif answer == 's':
            playing = False
            print('Player stands. Dealer is playing')
            break
        else:
            print('Incorrect input. Asking again..')
            continue


def show_some(player, dealer):
    print('Dealer hand is:')
    print('<card hidden>')
    print(dealer.cards[1])
    print('\nPlayer hand is:', *player.cards, sep='\n')


def show_all(player, dealer):
    print('Dealer hand is:', *dealer.cards, sep='\n')
    print('Dealer hands value: ', dealer.value)
    print('\nPlayer hand:', *player.cards, sep='\n')
    print('Player hands value:  ', player.value)


def player_busts(player, dealer, chips):
    print('Player busts!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('Dealer busts')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.lose_bet()


def push():
    print('Dealer and Player tie! It is a push')


def get_y_or_n(question):
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input(question)
    return answer


if __name__ == '__main__':

    while True:
        # Print an opening statement
        print('Welcome to play Black Jack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        player = Hand()
        player.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer = Hand()
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = player_chips if 'player_chips' in globals() else Chips()

        # Prompt the Player for their bet
        take_bet(player_chips)  # will modify player_chips.bet

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        while playing:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player)  # modifies playing and player

            # Show cards (but keep one dealer card hidden)
            show_some(player, dealer)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player.value > 21:
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)

        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)
        elif player.value > 21:
            player_busts(player, dealer, player_chips)
        elif dealer.value > player.value:
            player_busts(player, dealer, player_chips)
        elif dealer.value < player.value:
            dealer_busts(player, dealer, player_chips)
        else:  # tie
            push()

        # Inform Player of their chips total
        print(f'You have a total of {player_chips.chips} chips')

        if player_chips.chips > 0:
            # Ask to play again
            answer = get_y_or_n('Do you wanna play again? (y/n): ')
            if answer == 'y':
                playing = True
                continue
            else:
                print('Thanks for playing')
                break
        else:
            print('You ran out of chips. Buy more chips. Game is over!')
            break





