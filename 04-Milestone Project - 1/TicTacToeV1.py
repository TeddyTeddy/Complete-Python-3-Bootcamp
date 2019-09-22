# TASK:
# Implement TicTacToe game based on the rules:
# https://www.exploratorium.edu/brain_explorer/tictactoe.html

# initialize the game board (3x3) with empty squares on it
# empty values are initialized with -1
board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]


def display_board():
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


def is_valid_position(row, column):
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


def get_positional_indexes():
    # user enters the positional indexes
    row = int(input('Enter row index of the square you picked: '))
    column = int(input('Enter column index of the square you picked: '))
    while True:
        # check if the position is valid, if not continue
        check = is_valid_position(row, column)
        if check[0]:  # if the indexes are valid
            break
        else:
            print(check[1])   # the error string
            row = int(input('Enter row index of the square you picked: '))
            column = int(input('Enter column index of the square you picked: '))
    return row, column


def check_horizontal_win(turn):
    win = [turn] * 3
    return board[0] == win or board[1] == win or board[2] == win


def check_vertical_win(player):
    win = [player]*3
    column1 = [board[0][0], board[1][0], board[2][0]]
    column2 = [board[0][1], board[1][1], board[2][1]]
    column3 = [board[0][2], board[1][2], board[2][2]]
    return column1 == win or column2 == win or column3 == win


def check_diagonal_win(player):
    win = [player]*3
    diagonal_one = [board[0][0], board[1][1], board[2][2]]
    diagonal_two = [board[0][2], board[1][1], board[2][0]]
    return win == diagonal_one or win == diagonal_two


def no_free_square_left():
    return -1 not in board[0] and -1 not in board[1] and -1 not in board[2]


def is_winner(player):

    is_horizontal_win = False
    is_vertical_win = False
    is_diagonal_win = False

    # check horizontal wins
    is_horizontal_win = check_horizontal_win(player)
    if not is_horizontal_win:
        is_vertical_win = check_vertical_win(player)
        if not is_vertical_win:
            is_diagonal_win = check_diagonal_win(player)
    return is_diagonal_win or is_vertical_win or is_horizontal_win


def make_computer_move():

    # first, try to make a winning move if possible
    computer_made_the_move = False
    for row in [0, 1, 2]:
        for column in [0, 1, 2]:
            if board[row][column] == -1:  # if the square is empty
                board[row][column] = 'O'  # make a temporary computer move 'O'
                computer_made_the_move = is_winner('O')
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
                    board[row][column] = 'X'  # make a temporary user move 'X'
                    user_to_win = is_winner('X')
                    if user_to_win:
                        board[row][column] = 'O'  # make computer move to that winning square
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
        board[square_picked[0]][square_picked[1]] = 'O'  # make computer move on the square picked


def tic_tac_toe():
    # display the board
    display_board()
    # 'X' is user, 'O' is computer
    while True:

        # set 'X' to the board with valid position
        (row, column) = get_positional_indexes()

        # set user mark X to board
        board[row][column] = 'X'

        # if game ends, declare the winner end break
        if is_winner('X'):
            display_board()
            print(f'Winner is X')
            break
        elif no_free_square_left():
            # this is a tie
            print(f'This is a tie')
            break

        # X did not win, nor there is a tie
        make_computer_move()  # makes 'O' move

        # display the board
        display_board()

        # if game ends, declare the winner end break
        if is_winner('O'):
            print(f'Winner is O')
            break
        elif no_free_square_left():
            # this is a tie
            print(f'This is a tie')
            break


tic_tac_toe()
