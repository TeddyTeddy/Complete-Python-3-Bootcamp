import unittest
from my_zip import my_zip, MyZip


class MyZipGeneratorFunctionTest(unittest.TestCase):
    def test_non_iterables_passed(self):
        with self.assertRaises(TypeError):
            iterator= zip(1, 2, 3)
        with self.assertRaises(TypeError):
            iterator = my_zip(1, 2, 3)
            next(iterator)

    def test_empty_args(self):
        iterator = my_zip()  # must return an empty iterator
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_one_arg(self):
        my_set = {1, 2, 3}  # an iterable
        my_zip_iterator = my_zip(my_set)
        builtin_zip_iterator = zip(my_set)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))

    def test_two_args(self):
        my_set_1 = {1, 2, 3}        # an iterable (shortest)
        my_set_2 = {1, 2, 3, 4, 5}  # an iterable
        my_zip_iterator = my_zip(my_set_1, my_set_2)
        builtin_zip_iterator = zip(my_set_1, my_set_2)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))

    def test_three_args(self):
        my_set_1 = {1, 2, 3}        # an iterable
        my_set_2 = {1, 2, 3, 4, 5}  # an iterable
        my_list_1 = [0, 0]          # an iterable (shortest)
        my_zip_iterator = my_zip(my_set_1, my_set_2, my_list_1)
        builtin_zip_iterator = zip(my_set_1, my_set_2, my_list_1)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))

    def test_with_dictionaries(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'c': 4, 'd': 5}
        my_zip_iterator = my_zip(d1, d2)   # a generator to test
        builtin_zip_iterable = zip(d1, d2) # a builtin iterable to test againist
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterable))


class MyZipClassTest(unittest.TestCase):
    def test_non_iterables_passed(self):
        with self.assertRaises(TypeError):
            iterator= zip(1, 2, 3)
        with self.assertRaises(TypeError):
            iterator = MyZip(1, 2, 3)

    def test_empty_args(self):
        iterator = MyZip()  # must return an empty iterator
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_one_arg(self):
        my_set = {1, 2, 3}  # an iterable
        my_zip_iterator = MyZip(my_set)
        builtin_zip_iterator = zip(my_set)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))

    def test_two_args(self):
        my_set_1 = {1, 2, 3}        # an iterable (shortest)
        my_set_2 = {1, 2, 3, 4, 5}  # an iterable
        my_zip_iterator = MyZip(my_set_1, my_set_2)
        builtin_zip_iterator = zip(my_set_1, my_set_2)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))

    def test_three_args(self):
        my_set_1 = {1, 2, 3}        # an iterable
        my_set_2 = {1, 2, 3, 4, 5}  # an iterable
        my_list_1 = [0, 0]          # an iterable (shortest)
        my_zip_iterator = MyZip(my_set_1, my_set_2, my_list_1)
        builtin_zip_iterator = zip(my_set_1, my_set_2, my_list_1)  # A builtin zip class instance
        self.assertEqual(list(my_zip_iterator), list(builtin_zip_iterator))


if __name__ == '__main__':
    unittest.main()
