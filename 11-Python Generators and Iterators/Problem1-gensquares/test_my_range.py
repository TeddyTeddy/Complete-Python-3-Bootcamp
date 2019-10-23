import unittest
import gensquares


class TestMyRange(unittest.TestCase):
    def test_N_is_minus_two(self):
        test_iterator = gensquares.my_range(N=-2)  # iterator is my_range(N)
        print(test_iterator)
        self.assertEqual(next(test_iterator), [])
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_minus_one(self):
        test_iterator = gensquares.my_range(N=-1)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), [])
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_zero(self):
        test_iterator = gensquares.my_range(N=0)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), [])
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_one(self):
        test_iterator = gensquares.my_range(N=1)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_two(self):
        test_iterator = gensquares.my_range(N=2)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        self.assertEqual(next(test_iterator), 1)
        with self.assertRaises(StopIteration):
            next(test_iterator)

    def test_N_is_three(self):
        test_iterator = gensquares.my_range(N=3)  # iterator is my_range(N)
        self.assertEqual(next(test_iterator), 0)
        self.assertEqual(next(test_iterator), 1)
        self.assertEqual(next(test_iterator), 2)
        with self.assertRaises(StopIteration):
            next(test_iterator)


if __name__ == '__main__':
    unittest.main()
