"""
Does the following:
Step 1 - Building the data structures
     Opens 'restaurant_small.txt' for read-only and passes it to reader.read_restaurants()
    As a result, it receives NAME_TO_RATING, PRICE_TO_NAMES, CUISINE_TO_NAMES as such:

    NAME_TO_RATING = {'Georgie Porgie': 87, 'Queen St. Cafe': 82, 'Dumplings R Us': 71, 'Mexican Grill': 85,
                  'Deep Fried Everything': 52}
    PRICE_TO_NAMES = {'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'], '$$': ['Mexican Grill'],
                  '$$$': ['Georgie Porgie'], '$$$$': []}
    CUISINE_TO_NAMES = {'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'], 'Canadian': ['Georgie Porgie'],
                    'Malaysian': ['Queen St. Cafe'], 'Thai': ['Queen St. Cafe'], 'Chinese': ['Dumplings R Us'],
                    'Mexican': ['Mexican Grill']}

Step 2 - Filter By Price Range
    it selects the lowest price end restaurants as <NAMES_MATCHING_PRICE>

Step 3 - Filter By Cuisine For Those Names Matching The Price
    it initializes <SELECTED_CUISINES> as ['Tacos', 'Pub Food', 'Chinese']
    it then filters <NAMES_MATCHING_PRICE> via the <selected cuisines> ['Tacos', 'Pub Food', 'Chinese'] (refer to
    the call to NAMES_FINAL = filter_by_cuisine(...) call )

Step 4 - Sort and Return
    sort the NAMES_FINAL; refer to SORTED_FINAL = build_rating_list(names_matching, NAME_TO_RATING)  call
"""
import reader


def filter_by_cuisine(NAMES_MATCHING_PRICE, CUISINE_TO_NAMES, SELECTED_CUISINES):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    Return a list of the restaurants in NAMES_MATCHING_PRICE that serve at
    least one of the cuisines in SELECTED_CUISINES according to CUISINE_TO_NAMES.

    >>> NAMES_MATCHING_PRICE = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> CUISINE_TO_NAMES = {'Canadian': ['Georgie Porgie'],
                'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                'Malaysian': ['Queen St. Cafe'],
                'Thai': ['Queen St. Cafe'],
                'Chinese: ['Dumplings R Us'],
                'Mexican': ['Mexican Grill']}
    >>> SELECTED_CUISINES = ['Chinese', 'Thai']
    >>> filter_by_cuisine(NAMES_MATCHING_PRICE, CUISINE_TO_NAMES, SELECTED_CUISINES)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    result = set()  # set is chosen as an accumulator, because a restaurant may be added more than once to it
    for restaurant in NAMES_MATCHING_PRICE:
        for cuisine in SELECTED_CUISINES:
            if cuisine in CUISINE_TO_NAMES and restaurant in CUISINE_TO_NAMES[cuisine]:
                result.add(restaurant)  # .add() will prevent the addition of the same restaurant multiple times
    return list(result)


def build_rating_list(names_matching, NAME_TO_RATING):
    """ (list of str, dict of {str: int}) -> list of [int, str] list

    Return a list of [rating%, restaurant name], sorted by rating%.
    >>> NAME_TO_RATING = {'Georgie Porgie': 87,
                          'Queen St. Cafe': 82,
                          'Dumplings R Us': 71,
                          'Mexican Grill': 85,
                          'Deep Fried Everything': 52}
    >>> names_matching = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(names_matching, NAME_TO_RATING)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    result = []
    for name in names_matching:
        if name in NAME_TO_RATING:  # to make sure that name key exists in NAME_TO_RATING dict
            result.append([NAME_TO_RATING[name], name])
    result.sort(reverse=True)  # sort in descending order; i.e highest rating first
    return result


if __name__ == '__main__':
    # STEP 1 - Building the data structures
    FILE = open('restaurant_small.txt', 'r')
    NAME_TO_RATING, PRICE_TO_NAMES, CUISINE_TO_NAMES = reader.read_restaurants(FILE)
    FILE.close()

    print(f'NAME_TO_RATING = {NAME_TO_RATING}')
    print(f'PRICE_TO_NAMES = {PRICE_TO_NAMES}')
    print(f'CUISINE_TO_NAMES = {CUISINE_TO_NAMES}')

    # STEP 2 - Filter By Price Range
    PRICE = '$'
    NAMES_MATCHING_PRICE = PRICE_TO_NAMES[PRICE]
    print(f'NAMES_MATCHING_PRICE = {NAMES_MATCHING_PRICE}')

    # STEP 3 - Filter By Cuisine For Those Names Matching The Price
    SELECTED_CUISINES = ['Tacos', 'Pub Food', 'Chinese']  # note that 'Tacos' is not a served cuisine in any restaurant
    print(f'SELECTED_CUISINES = {SELECTED_CUISINES}')
    NAMES_FINAL = filter_by_cuisine(NAMES_MATCHING_PRICE, CUISINE_TO_NAMES, SELECTED_CUISINES)
    print(f'NAMES_FINAL = {NAMES_FINAL}')

    # STEP 4 - Sort and Return
    SORTED_FINAL = build_rating_list(NAMES_FINAL, NAME_TO_RATING)
    print(f'SORTED_FINAL = {SORTED_FINAL}')
