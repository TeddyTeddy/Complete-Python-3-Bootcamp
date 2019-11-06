locations = {0: 'Exit',
             1: 'On the road',
             2: 'On the hill',
             3: 'In a building',
             4: 'In a valley',
             5: 'In a forest'}

exits = [{'Q': 0},
         {'W': 2, 'E': 3, 'N': 5, 'S': 4, 'Q': 0},  # for 1 Road
         {'N': 5, 'Q': 0},                          # for 2 Hill
         {'W': 1, 'Q': 0},                          # for 3 Building
         {'W': 2, 'N': 1, 'Q': 0},                  # for 4 Valley
         {'W': 2, 'S': 1, 'Q': 0}]                  # for 5 Forest


def play_game():
    location = 1
    while True:
        # get all the directions available for location
        available_directions = ', '.join(exits[location].keys())  # i.e. W, E, N, S, Q
        print(locations[location])                      # i.e. 'On the road'
        if location == 0:
            break
        print('Available directions: ' + available_directions)
        selected_direction = input('Enter selected direction: ').upper()
        if selected_direction in available_directions:
            location = exits[location][selected_direction]
        else:
            print('That direction is not available for this location')


if __name__ == '__main__' :
    play_game()
