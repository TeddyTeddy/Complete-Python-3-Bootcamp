import unittest
import reader
from application import filter_by_cuisine
from application import build_rating_list


class TestFilterByCuisine(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        file = open('restaurant_small.txt', 'r')
        self._name_to_rating, self._price_to_names, self._cuisine_to_names = reader.read_restaurants(file)
        file.close()

    def test_no_restaurants_for_selected_cuisines(self):
        """
        In case selected cuisines are not served by any restaurant, then filter_by_cuisine()
        must return an empty list
        :return: none
        """
        price = '$'
        names_matching_price = self._price_to_names[price]
        selected_cuisines = ['Turkish', 'Vietnamese', 'Indian']  # none of these cuisines are in the file
        names_final = filter_by_cuisine(names_matching_price, self._cuisine_to_names, selected_cuisines)
        self.assertEqual(names_final, [])

    def test_a_restaurant_serving_multiple_selected_cuisines(self):
        """
        In case more than one selected cuisines are served by a restaurant, then
        filter_by_cuisine() returns the restaurant name only once
        :return: none
        """
        price = '$$$'
        names_matching_price = self._price_to_names[price]
        selected_cuisines = ['Canadian', 'Pub Food', 'Indian']  # 'Indian' cuisine is not in the file
        # note: the restaurant 'Georgie Porgie' serves both 'Canadian' and 'Pub Food'
        names_final = filter_by_cuisine(names_matching_price, self._cuisine_to_names, selected_cuisines)
        for name in names_final:
            self.assertEqual(names_final.count(name), 1)

    def test_restaurants_serving_one_of_the_selected_cuisine(self):
        """
        In case there are restaurants serving only one of the selected cuisines, then
        filter_by_cuisine() must return those restaurants
        :return: none
        """
        price = '$'
        names_matching_price = self._price_to_names[price]
        # names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']

        selected_cuisines = ['Pub Food', 'Thai', 'Vietnamese']  # Vietnamese is not in the file
        names_final = filter_by_cuisine(names_matching_price, self._cuisine_to_names, selected_cuisines)
        self.assertEqual(names_final.sort(), ['Deep Fried Everything', 'Queen St. Cafe'].sort())

    def test_no_restaurants_matching_the_price(self):
        """
        In case names_matching_price is an empty list, filter_by_cuisine() must return an empty list
        :return: none
        """
        price = '$$$$'
        names_matching_price = self._price_to_names[price]  # i.e. an empty list
        selected_cuisines = ['Pub Food', 'Thai', 'Vietnamese']  # Vietnamese is not in the file
        names_final = filter_by_cuisine(names_matching_price, self._cuisine_to_names, selected_cuisines)
        self.assertEqual(names_final, [])

    def test_empty_selected_cuisines_list_passed(self):
        """
        In case selected_cuisines list is empty, filter_by_cuisine() must return an empty list
        :return: none
        """
        price = '$'
        names_matching_price = self._price_to_names[price]
        # names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']

        selected_cuisines = []  # none of these cuisines are in the file
        names_final = filter_by_cuisine(names_matching_price, self._cuisine_to_names, selected_cuisines)
        self.assertEqual(names_final, [])

    def test_empty_cuisine_to_names_dict_passed(self):
        """
        In case cuisine_to_names dictionary is empty, filter_by_cuisine() must return an empty list
        :return: none
        """
        price = '$'
        names_matching_price = self._price_to_names[price]
        # names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']

        selected_cuisines = ['Pub Food', 'Thai', 'Vietnamese']  # Vietnamese is not in the file
        cuisine_to_names = {}
        names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, selected_cuisines)
        self.assertEqual(names_final, [])


class TestBuildRatingList(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        file = open('restaurant_small.txt', 'r')
        self._name_to_rating, self._price_to_names, self._cuisine_to_names = reader.read_restaurants(file)
        file.close()

    def test_empty_names_matching_list_passed(self):
        """
        In case names_matching list is empty, build_rating_list() returns an empty list
        :return: None
        """
        names_matching = []
        sorted_rating_list = build_rating_list(names_matching, self._name_to_rating)
        self.assertEqual(sorted_rating_list, [])

    def test_five_names_matching(self):
        """
        In case all 5 restaurants are in names_matching list, then build_rating_list() returns a sorted list
        of [int, str] lists
        :return:
        """
        names_matching = ['Georgie Porgie', 'Queen St. Cafe', 'Dumplings R Us', 'Mexican Grill', 'Deep Fried Everything']
        sorted_rating_list = build_rating_list(names_matching, self._name_to_rating)
        expected_sorted_rating_list = [[87, 'Georgie Porgie'], [85, 'Mexican Grill'], [82, 'Queen St. Cafe'],
                                       [71, 'Dumplings R Us'], [52, 'Deep Fried Everything']]
        self.assertEqual(sorted_rating_list, expected_sorted_rating_list)

    def test_three_names_matching(self):
        """
        In case 3 restaurants are in names_matching list, then build_rating_list() returns a sorted list
        of [int, str] lists
        :return:
        """
        names_matching = ['Queen St. Cafe', 'Mexican Grill', 'Deep Fried Everything']
        sorted_rating_list = build_rating_list(names_matching, self._name_to_rating)
        expected_sorted_rating_list = [[85, 'Mexican Grill'], [82, 'Queen St. Cafe'], [52, 'Deep Fried Everything']]
        self.assertEqual(sorted_rating_list, expected_sorted_rating_list)

    def test_one_name_matching(self):
        """
        In case  only 1 restaurants is in names_matching list, then build_rating_list() returns a sorted list
        of [int, str] list
        :return:
        """
        names_matching = ['Queen St. Cafe']
        sorted_rating_list = build_rating_list(names_matching, self._name_to_rating)
        expected_sorted_rating_list = [[82, 'Queen St. Cafe']]
        self.assertEqual(sorted_rating_list, expected_sorted_rating_list)


if __name__ == '__main__':
    unittest.main()
