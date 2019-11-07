from read_restaurants import read_restaurants


def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    Return a list of the restaurants in names_matching_price that serve at
    least one of the cuisines in cuisines_list according to cuisine_to_names.

    >>> names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuisine_to_names = {'Canadian': ['Georgie Porgie'],
                'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
                'Malaysian': ['Queen St. Cafe'],
                'Thai': ['Queen St. Cafe'],
                'Chinese: ['Dumplings R Us'],
                'Mexican': ['Mexican Grill']}
    >>> cuisines_list = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    result = set()  # set is chosen, because a restaurant may be added more than once to the result
    for restaurant in names_matching_price:
        for cuisine in cuisines_list:
            if cuisine in cuisine_to_names and restaurant in cuisine_to_names[cuisine]:
                result.add(restaurant)  # .add() will prevent the addition of the same restaurant multiple times
    return list(result)


def build_rating_list(names_matching, name_to_rating):
    """ (list of str, dict of {str: int}) -> list of [int, str] list

    Return a list of [rating%, restaurant name], sorted by rating%.
    >>> name_to_rating = {'Georgie Porgie': 87,
                          'Queen St. Cafe': 82,
                          'Dumplings R Us': 71,
                          'Mexican Grill': 85,
                          'Deep Fried Everything': 52}
    >>> names_matching = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(names_matching, name_to_rating)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    result = []
    for name in names_matching:
        if name in name_to_rating:  # to make sure that name key exists in name_to_rating dict
            result.append([name_to_rating[name], name])
    result.sort(reverse=True)
    return result


if __name__ == '__main__':
    file = open('restaurant_small.txt', 'r')
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)
    file.close()

    print(f'name_to_rating = {name_to_rating}')
    print(f'price_to_names = {price_to_names}')
    print(f'cuisine_to_names = {cuisine_to_names}')

    price = '$'
    names_matching_price = price_to_names[price]
    print(f'names_matching_price = {names_matching_price}')

    cuisines_list = ['Tacos', 'Pub Food', 'Chinese']  # note that 'Tacos' is not a supported cuisine
    print(f'cuisines_list = {cuisines_list}')
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    print(f'names_final = {names_final}')

    sorted_final = build_rating_list(names_final, name_to_rating)
    print(f'sorted_final = {sorted_final}')
