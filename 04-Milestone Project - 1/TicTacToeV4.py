# TASK:
# Implement TicTacToe game based on the rules:
# https://www.exploratorium.edu/brain_explorer/tictactoe.html


def display_board(board):
    print('Current status:')
    print('    0  1  2')
    for row in [0, 1, 2]:
        row_str = f'{row}  '
        for column in [0, 1, 2]:
            if board[row][column] == -1:
                row_str += '[ ]'
            else:
                row_str += f'[{board[row][column]}]'
        print(row_str)


def is_valid_position(row, column, board):
    result = [True]
    if row not in [0, 1, 2] and column not in [0, 1, 2]:
        result = [False, 'Both indexes are invalid. They must be one of these: [0, 1, 2]']
    elif row not in [0, 1, 2]:
        result = [False, 'Row index is invalid. It must be one of these: [0, 1, 2]']
    elif column not in [0, 1, 2]:
        result = [False, 'Column index is invalid. It must be one of these: [0, 1, 2]']
    elif board[row][column] != -1:
        result = [False, 'The chosen square is not empty']
    return result


def get_positional_indexes(board):
    # user enters the positional indexes
    row = int(input('Enter row index of the square you picked: '))
    column = int(input('Enter column index of the square you picked: '))
    while True:
        # check if the position is valid, if not continue
        check = is_valid_position(row, column, board)
        if check[0]:  # if the indexes are valid
            break
        else:
            print(check[1])   # the error string
            row = int(input('Enter row index of the square you picked: '))
            column = int(input('Enter column index of the square you picked: '))
    return row, column


def no_free_square_left(board):
    return -1 not in board[0] and -1 not in board[1] and -1 not in board[2]


def is_winner(player, board):

    # check horizontal wins
    win = [player] * 3   # ['X', 'X', 'X'] or ['0', 'O', 'O']
    return ((board[0] == win) or   # horizontal top
           (board[1] == win) or   # horizontal middle
           (board[2] == win) or   # horizontal bottom
           ([board[0][0], board[1][0], board[2][0]] == win) or  # vertical left
           ([board[0][1], board[1][1], board[2][1]] == win) or  # vertical middle
           ([board[0][2], board[1][2], board[2][2]] == win) or # vertical right
           ([board[0][0], board[1][1], board[2][2]] == win) or # diagonal
           ([board[0][2], board[1][1], board[2][0]] == win))   # diagonal


def make_computer_move(players, board):

    # first, try to make a winning move if possible
    computer_made_the_move = False
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
            if board[row][column] == -1:  # if the square is empty
                board[row][column] = players["computer"]  # make a temporary computer move
                computer_made_the_move = is_winner(players["computer"], board)
                if computer_made_the_move:
                    break
                else:                      # revert back the temporary move
                    board[row][column] = -1
        if computer_made_the_move:
            break

    # if there is no winning move possible by the computer, try to block the opponent
    if not computer_made_the_move:
        for row in [0, 1, 2]:
            for column in [0, 1, 2]:
                if board[row][column] == -1:  # if the square is empty
                    board[row][column] = players["user"]  # make a temporary user move
                    user_to_win = is_winner(players["user"], board)
                    if user_to_win:
                        board[row][column] = players["computer"]  # make computer move to that winning square
                        computer_made_the_move = True
                        break
                    else:
                        board[row][column] = -1  # revert back the temporary move
            if computer_made_the_move:
                break

    # if neither computer nor user is winning, then make a move based on the square's priorities
    if not computer_made_the_move:
        square_picked = ()
        current_priority_level = -1
        square_priorities = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
        for row in [0, 1, 2]:
            for column in [0, 1, 2]:
                is_square_empty = board[row][column] == -1
                squares_priority = square_priorities[row][column]
                if is_square_empty and current_priority_level < squares_priority:
                    current_priority_level = squares_priority
                    square_picked = (row, column)
        board[square_picked[0]][square_picked[1]] = players["computer"]  # make computer move on the square picked


def choose_player():
    user = '-1'
    computer = '-1'
    user = input("Please pick a marker 'X' or 'O': ").upper()
    while user != 'X' and user != 'O':
        user = input("Incorrect choice. Please pick a marker 'X' or 'O'").upper()
    computer = 'O' if user == 'X' else 'X'
    players = {'user': user, 'computer': computer}
    return players


def tic_tac_toe():

    # initialize the game board (3x3) with empty squares on it
    # empty squares are marked with -1
    board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

    players = choose_player()

    if players['user'] == 'X':
        # display the board
        display_board(board)

        while True:

            # set user to the board with valid position
            (row, column) = get_positional_indexes(board)

            # set user mark X to board
            board[row][column] = players['user']

            # if game ends, declare the winner end break
            if is_winner(players['user'], board):
                display_board(board)
                print(f'Winner is {players["user"]}')
                break
            elif no_free_square_left(board):
                # this is a tie
                display_board(board)
                print(f'This is a tie')
                break

            # X did not win, nor there is a tie
            make_computer_move(players, board)  # makes players["computer"] move

            # display the board
            display_board(board)

            # if game ends, declare the winner end break
            if is_winner(players["computer"], board):
                print(f'Winner is {players["computer"]}')
                break

    else:  # Computer is 'X' and it starts first
        while True:

            make_computer_move(players, board)  # makes players["computer"] move

            # display the board
            display_board(board)

            # if game ends, declare the winner end break
            if is_winner(players["computer"], board):
                print(f'Winner is {players["computer"]}')
                break
            elif no_free_square_left(board):
                # this is a tie
                print(f'This is a tie')
                break

            # set user to the board with valid position
            (row, column) = get_positional_indexes(board)

            # set user mark X to board
            board[row][column] = players['user']

            # if game ends, declare the winner end break
            if is_winner(players['user'], board):
                display_board(board)
                print(f'Winner is {players["user"]}')
                break


tic_tac_toe()
