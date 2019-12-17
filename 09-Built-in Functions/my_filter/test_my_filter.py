import unittest
from my_filter import MyFilter


class MyFilterCase(unittest.TestCase):
    """
    MyFilter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            iterator = filter()
        with self.assertRaises(TypeError):
            iterator = MyFilter()

    def test_non_iterable(self):
        non_iterable = 1  # int is not iterable
        with self.assertRaises(TypeError):
            iterator = filter(None, non_iterable)
        with self.assertRaises(TypeError):
            iterator = MyFilter(None, non_iterable)

    def test_not_callable(self):
        func = 1  # not callable
        iterable = [1, 2, 3]
        reference_iterator = filter(func, iterable)
        under_test_iterator = MyFilter(func, iterable)
        with self.assertRaises(TypeError):
            ignored = next(reference_iterator)
        with self.assertRaises(TypeError):
            ignored = next(under_test_iterator)

    def test_None_func_and_iterable(self):
        func = None
        iterable = [False, True, 1, 0, 3]
        reference_iterator = filter(func, iterable)
        under_test_iterator = MyFilter(func, iterable)
        self.assertEqual(list(reference_iterator), list(under_test_iterator))

    def test_False_func_and_iterable(self):
        iterable = [False, True, 1, 0, 3]
        reference_iterator = filter(lambda x: False, iterable)
        under_test_iterator = MyFilter(lambda x: False, iterable)
        self.assertEqual(list(reference_iterator), list(under_test_iterator))

    def test_True_func_and_iterable(self):
        iterable = [False, True, 1, 0, 3]
        reference_iterator = filter(lambda x: True, iterable)
        under_test_iterator = MyFilter(lambda x: True, iterable)
        self.assertEqual(list(reference_iterator), list(under_test_iterator))

    def test_even_func_and_iterable(self):
        iterable = range(0, 10)
        reference_iterator = filter(lambda x: x % 2 == 0, iterable)
        under_test_iterator = MyFilter(lambda x: x % 2 == 0, iterable)
        # print(list(reference_iterator))
        # print(list(under_test_iterator))
        self.assertEqual(list(reference_iterator), list(under_test_iterator))


if __name__ == '__main__':
    unittest.main()
