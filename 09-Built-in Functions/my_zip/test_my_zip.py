import unittest
from my_zip import my_zip
from my_zip import MyZip

class MyZipGeneratorFunctionTest(unittest.TestCase):
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


class MyZipClassTest(unittest.TestCase):
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
