import unittest
import gensquares


class TestMyRange(unittest.TestCase):
    def test_N_is_minus_two(self):
        """
        >>> iterable = range(-2)
        >>> iterator = iter(iterable)
        >>> next(iterator)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration
        """
        test_iterator = gensquares.my_range(-2)  # iterator is my_range(N)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_minus_one(self):
        """
        >>> iterable = range(-1)
        >>> iterator = iter(iterable)
        >>> next(iterator)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration
        """
        test_iterator = gensquares.my_range(-1)  # iterator is my_range(N)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_zero(self):
        """
        >>> iterable = range(0)
        >>> iterator = iter(iterable)
        >>> next(iterator)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration
        """
        test_iterator = gensquares.my_range(0)  # iterator is my_range(N)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_one(self):
        test_iterator = gensquares.my_range(1)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_two(self):
        test_iterator = gensquares.my_range(2)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        self.assertEqual(next(test_iterator), 1)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_three(self):
        test_iterator = gensquares.my_range(3)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        self.assertEqual(next(test_iterator), 1)
        self.assertEqual(next(test_iterator), 2)
        with self.assertRaises(StopIteration):
            next(test_iterator)


if __name__ == '__main__':
    unittest.main()
