# modify game_v2.py so that it uses the new augmented 'locations' dictionary
locations = {'EXIT': {'desc': 'On the exit',
                      'exits': {}},
             'ROAD': {'desc': 'On the road',
                      'exits': {'W': 'HILL', 'HILL': 'HILL', 'E': 'BUILDING', 'BUILDING': 'BUILDING', 'N': 'FOREST',
                                'FOREST': 'FOREST', 'S': 'VALLEY', 'VALLEY': 'VALLEY', 'Q': 'EXIT'}},
             'HILL': {'desc': 'On the hill',
                      'exits': {'N': 'FOREST', 'FOREST': 'FOREST', 'Q': 'EXIT'}},
             'BUILDING': {'desc': 'In a building',
                          'exits': {'W': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'}},
             'VALLEY': {'desc': 'In a valley',
                        'exits': {'W': 'HILL', 'HILL': 'HILL', 'N': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'}},
             'FOREST': {'desc':'In a forest',
                        'exits': {'W': 'HILL', 'HILL': 'HILL', 'S': 'ROAD', 'ROAD': 'ROAD', 'Q': 'EXIT'}}
             }

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
        available_exits = ', '.join(locations[location_key]['exits'].keys())  # i.e. 'W, HILL, E, BUILDING, N, FOREST, S, VALLEY, Q'
        print(f'** Your current location: {locations[location_key]["desc"]}')  # i.e. 'On the road'
        if location_key == 'EXIT':
            break
        print('Available exits: ' + available_exits)
        selected_exit = input('Enter selected exits: ').upper()  # user can enter any text here
        if selected_exit in vocabulary:
            selected_exit = vocabulary[selected_exit]
            if selected_exit in available_exits:
                location_key = locations[location_key]['exits'][selected_exit]
            else:
                print(f'{selected_exit} is not available in your current location')
        else:
            print(f'{selected_exit} is not a valid a direction ')


if __name__ == '__main__' :
    play_game()
