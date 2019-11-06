# modify game_v1.py so that the exits is a dictionary rather than a list
# with the keys being the numbers of the location_keys and the values being
# dictionaries holding the keys (as they do at present). No change should be
# needed in play_game() code.

# Once that is working, create another dictionary that contains words that
# players may use when entering the direction. These words will be the keys,
# and their values will be a single letter that program may determine which way
# to go
locations = {0: 'Exit',
             1: 'On the road',
             2: 'On the hill',
             3: 'In a building',
             4: 'In a valley',
             5: 'In a forest'}

exits = {0: {'Q': 0},
         1: {'W': 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},  # for 1 Road
         2: {'N': 5, 'Q': 0},                          # for 2 Hill
         3: {'W': 1, 'Q': 0},                          # for 3 Building
         4: {'W': 2, 'N': 1, 'Q': 0},                  # for 4 Valley
         5: {'W': 2, 'S': 1, 'Q': 0}}                  # for 5 Forest

vocabulary = {'EAST': 'E',  # keys: possible text entries, values: Q,W,E,S,N letters which are key values
              'WEST': 'W',  # in exits dict
              'NORTH': 'N',
              'SOUTH': 'S',
              'QUIT': 'Q'}


def play_game():
    location_key = 1
    while True:
        # get all the directions available for location_key
        available_directions = ', '.join(exits[location_key].keys())  # i.e. 'W, E, N, S, Q'
        print(f'** Your current location: {locations[location_key]}')                      # i.e. 'On the road'
        if location_key == 0:
            break
        print('Available directions: ' + available_directions)
        selected_direction = input('Enter selected direction (east/west/north/south): ').upper()  # user can enter any text here
        if selected_direction in vocabulary:
            selected_direction = vocabulary[selected_direction]  # mapped to a letter Q, W, E, S, N as a key
            if selected_direction in available_directions:
                location_key = exits[location_key][selected_direction]
            else:
                print(f'{selected_direction} is not available in your current location')
        else:
            print(f'{selected_direction} is not a valid a direction ')


if __name__ == '__main__' :
    play_game()
