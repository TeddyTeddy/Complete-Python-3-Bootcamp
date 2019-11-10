# modify game_v1.py so that the exits is a dictionary rather than a list
# with the keys being the numbers of the location_keys and the values being
# dictionaries holding the keys (as they do at present). No change should be
# needed in play_game() code.

# Once that is working, create another dictionary that contains words that
# players may use when entering the direction. These words will be the keys,
# and their values will be a single letter that program may determine which way
# to go
locations = {'EXIT': 'On the exit',
             'ROAD': 'On the road',
             'HILL': 'On the hill',
             'BUILDING': 'In a building',
             'VALLEY': 'In a valley',
             'FOREST': 'In a forest'}

exits = {'EXIT': {'Q': 'EXIT'},
         'ROAD': {'W': 'HILL', 'HILL': 'HILL', 'E': 'BUILDING', 'BUILDING': 'BUILDING', 'N': 'FOREST',
                  'FOREST': 'FOREST', 'S': 'VALLEY', 'VALLEY': 'VALLEY', 'Q': 'EXIT'},
         'HILL': {'N': 'FOREST', 'FOREST': 'FOREST', 'Q': 'EXIT'},
         'BUILDING': {'W': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'},
         'VALLEY': {'W': 'HILL', 'HILL': 'HILL', 'N': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'},
         'FOREST': {'W': 'HILL', 'HILL': 'HILL', 'S': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'}}

vocabulary = {'EAST': 'E',  # keys: possible text entries, values: Q,W,E,S,N letters which are key values
              'WEST': 'W',  # in exits dict
              'NORTH': 'N',
              'SOUTH': 'S',
              'QUIT': 'Q',
              'ROAD': 'ROAD',
              'HILL': 'HILL',
              'BUILDING': 'BUILDING',
              'VALLEY': 'VALLEY',
              'FOREST': 'FOREST',
              'E': 'E',
              'S': 'S',
              'W': 'W',
              'N': 'N',
              'Q': 'Q',
              'EXIT': 'Q'}


def play_game():
    location_key = 'ROAD'
    while True:
        # get all the directions available for location_key
        available_exits = ', '.join(exits[location_key].keys())  # i.e. 'W, HILL, E, BUILDING, N, FOREST, S, VALLEY, Q'
        print(f'** Your current location: {locations[location_key]}')                      # i.e. 'On the road'
        if location_key == 'EXIT':
            break
        print('Available exits: ' + available_exits)
        selected_exit = input('Enter selected exits: ').upper()  # user can enter any text here
        if selected_exit in vocabulary:
            selected_exit = vocabulary[selected_exit]
            if selected_exit in available_exits:
                location_key = exits[location_key][selected_exit]
            else:
                print(f'{selected_exit} is not available in your current location')
        else:
            print(f'{selected_exit} is not a valid a direction ')


if __name__ == '__main__' :
    play_game()
