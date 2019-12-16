import unittest
from my_map import my_map, get_total


class TestMyMapCase(unittest.TestCase):
    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            iterator = my_map()
            next(iterator)

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            iterator = my_map(lambda x: x**2)
            next(iterator)

    def test_first_argument_is_not_callable(self):
        """
        map(func, *iterables) –> map object
        test that when func is not callable, my_map raises TypeError
        """
        with self.assertRaises(TypeError):
            lst = [1, 2, 3]  # not callable
            iterator = my_map(lst, lst)
            next(iterator)

    def test_passed_non_iterable(self):
        """
        map(func, *iterables) –> map object
        test that when iterables contain a non-iterable (i.e. int), my_map raises TypeError
        """
        with self.assertRaises(TypeError):
            non_iterable = 1  # int is non-iterable
            iterator = my_map(lambda x: x**2, non_iterable)
            next(iterator)

    def test_three_iterables_with_same_length(self):
        list_1 = [1, 2, 3]  # an iterable
        list_2 = [5, 2, 4]  # an iterable
        list_3 = [7, 7, 7]  # an iterable
        generator = my_map(get_total, list_1, list_2, list_3)
        expected_list = [13, 11, 14]
        self.assertEqual(expected_list, list(generator))

    def test_three_iterables_with_different_lengths(self):
        """
        to test that my_map raises StopIteration when the shortest iterable (i.e. list_2) is consumed
        """
        list_1 = [1, 2, 3, 4, 5]        # an iterable
        list_2 = [5, 2, 4]              # the shortest iterable
        list_3 = [7, 7, 7, 7, 7, 7]     # an iterable
        generator = my_map(get_total, list_1, list_2, list_3)
        expected_list = [13, 11, 14]
        self.assertEqual(expected_list, list(generator))


if __name__ == '__main__':
    unittest.main()
