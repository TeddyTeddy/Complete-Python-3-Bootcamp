"""
A module which is used to read the contents of the file 'restaurant_small.txt'
"""


class ReadingState:
    """
    A helper class. It has a state information starting with NAME and going
    circularly NAME -> RATING -> PRICE -> CUISINES -> NAME -> RATING ... and so on.
    State information tells what kind of line (in the file) we expect to read (i.e. RATING, 82%)
    so that we can process that line and return the result accordingly i.e. tuple (RATING, 82)
    """
    def __init__(self):
        self._state = 'NAME'
        self._next = {'NAME': 'RATING', 'RATING': 'PRICE', 'PRICE': 'CUISINES', 'CUISINES': 'NAME'}

    def identify(self, line):
        """
        Given a line str, identify() tells the line-type and the processed value stored in the line
        :param line: (str) a line to be identified as NAME/RATING/PRICE or CUISINES (i.e. <line-type>
        :return: (tuple) of <line-type>, value: i.e.
                            NAME, restaurant-name (str)
                            RATING, restaurant_rating (int)
                            PRICE, restaurant-price (str)
                            CUISINES, a tuple of (cuisine1, cuisine2, ...)
        """
        expecting = self._state
        self._state = self._next[self._state]  # set the state for the next call to .identify()
        if expecting == 'NAME':
            result = 'NAME', line
        elif expecting == 'RATING':
            result = 'RATING', int(line.replace('%', ''))
        elif expecting == 'PRICE':
            result = 'PRICE', line
        elif expecting == 'CUISINES':
            result = 'CUISINES', tuple(line.split(', '))
        else:
            raise NotImplementedError  # our state machine is broken
        return result


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
    reading_state = ReadingState()

    for line in file:
        line = line.replace('\n', '')       # remove "\n" from the line
        line_type, value = reading_state.identify(line)
        # print(f'{line_type}, {value}')

        # construct a dict of {restaurant name: rating%}
        if line_type == 'NAME':
            restaurant_name = value  # value holds the name of the restaurant
        elif line_type == 'RATING':
            name_to_rating[restaurant_name] = value  # value holds the rating

        # construct a dict of {price range (str): list of restaurant names (str)}
        if line_type == 'PRICE':
            price_to_names[value].append(restaurant_name)  # value holds the price

        # construct a dict of {cuisine: list of restaurant names}
        if line_type == 'CUISINES':
            for cuisine in value:  # value is a tuple containing cuisines i.e. ('Pub Food', 'Canadian')
                if cuisine in cuisine_to_names:  # we already added an item; cuisine: list of restaurant names
                    cuisine_to_names[cuisine].append(restaurant_name)
                else:  # cuisine is NOT in cuisine_to_name; i.e. a new cuisine
                    cuisine_to_names[cuisine] = [restaurant_name]

    return name_to_rating, price_to_names, cuisine_to_names
