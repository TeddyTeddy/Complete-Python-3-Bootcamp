class ReadState:
    def __init__(self):
        self._state = 'NAME'
        self._next = {'NAME': 'RATING', 'RATING': 'PRICE', 'PRICE': 'CUISINES', 'CUISINES': 'NAME'}

    def identify(self, line):
        current_state = self._state
        self._state = self._next[self._state]  # set the state for the next call to .identify()
        if current_state == 'NAME':
            return 'NAME', line
        elif current_state == 'RATING':
            return 'RATING', int(line.replace('%', ''))
        elif current_state == 'PRICE':
            return 'PRICE', line
        elif current_state == 'CUISINES':
            return 'CUISINES', tuple(line.split(', '))


def read_restaurants(file):
    """ (file) -> (dict of {str: int}, dict of {str: list of str}, dict of {str: list of str})

    Return a tuple of three dictionaries based on the information in file:

    - a dict of {restaurant name: rating%}
    - a dict of {price range: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}
    read_state = ReadState()

    for line in file:
        line = line.replace('\n', '')       # remove "\n" from the line
        line_type, value = read_state.identify(line)
        # print(f'{line_type}, {value}')

        # construct a dict of {restaurant name: rating%}
        if line_type == 'NAME':
            restaurant_name = value  # value holds the name of the restaurant
        elif line_type == 'RATING':
            name_to_rating[restaurant_name] = value  # value holds the rating

        # construct a dict of {price range: list of restaurant names}
        if line_type == 'PRICE':
            price_to_names[value].append(restaurant_name)

        # construct a dict of {cuisine: list of restaurant names}
        if line_type == 'CUISINES':
            for cuisine in value:  # value holds cuisines tuple i.e. ('Pub Food', 'Canadian')
                if cuisine in cuisine_to_names:  # we already added an item; cuisine: list of restaurant names
                    cuisine_to_names[cuisine].append(restaurant_name)
                else:  # cuisine is NOT in cuisine_to_name
                    cuisine_to_names[cuisine] = [restaurant_name]

    return name_to_rating, price_to_names, cuisine_to_names

