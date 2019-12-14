import unittest
from my_islice import my_islice, fibonacci
from itertools import islice


class MyIsSliceTestCase(unittest.TestCase):
    def test_zero_arguments_passed(self):
        with self.assertRaises(TypeError):
            iterator = islice()
        with self.assertRaises(TypeError):
            iterator = my_islice()  # returns a generator
            next(iterator)

    def test_one_argument_passed(self):
        with self.assertRaises(TypeError):
            iterator = islice(fibonacci())
        with self.assertRaises(TypeError):
            iterator = my_islice(fibonacci())  # returns a generator
            next(iterator)

    def test_five_arguments_passed(self):
        with self.assertRaises(TypeError):
            iterator = islice(fibonacci(), 0, 10, 2, 5)
        with self.assertRaises(TypeError):
            iterator = my_islice(fibonacci(), 0, 10, 2, 5)
            next(iterator)

    def test_not_iterable_passed(self):
        with self.assertRaises(TypeError):
            iterator = islice(3, 0, 10, 2)
        with self.assertRaises(TypeError):
            iterator = my_islice(3, 0, 10, 2)
            next(iterator)

    def test_stop_is_none(self):
        """
        my_islice(iterable, stop) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        reference_iterator = islice(iterable, None)
        under_test_generator = my_islice(iterable, None)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

        iterable = []
        reference_iterator = islice(iterable, None)
        under_test_generator = my_islice(iterable, None)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_stop_is_not_int_and_not_None(self):
        """
        my_islice(iterable, stop) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_stop = 3.14
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, bad_stop)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, bad_stop)
            next(under_test_generator)

    def test_start_is_not_int_and_not_None(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_start = 3.14
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, bad_start, 10)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, bad_start, 10)
            next(under_test_generator)

    def test_start_is_negative_int(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_start = -1
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, bad_start, 10)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, bad_start, 10)
            next(under_test_generator)

    def test_step_is_float(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_step = 3.14
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, 1, 10, bad_step)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, 1, 10, bad_step)
            next(under_test_generator)

    def test_step_is_zero(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_step = 0
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, 1, 10, bad_step)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, 1, 10, bad_step)
            next(under_test_generator)

    def test_step_is_negative(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bad_step = -30
        with self.assertRaises(ValueError):
            reference_iterator = islice(iterable, 1, 10, bad_step)

        with self.assertRaises(ValueError):
            under_test_generator = my_islice(iterable, 1, 10, bad_step)
            next(under_test_generator)


    def test_two_valid_args_passed(self):
        """
        my_islice(iterable, stop) --> my_islice generator
        """
        reference_iterator = islice(fibonacci(), 10)
        under_test_generator = my_islice(fibonacci(), 10)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_three_valid_args_passed(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        reference_iterator = islice(fibonacci(), 3, 10)
        under_test_generator = my_islice(fibonacci(), 3, 10)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_four_valid_args_passed(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        reference_iterator = islice(fibonacci(), 3, 20, 3)
        under_test_generator = my_islice(fibonacci(), 3, 20, 3)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

        reference_iterator = islice(fibonacci(), 3, 20, 2)
        under_test_generator = my_islice(fibonacci(), 3, 20, 2)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_start_pointing_beyond_the_end_of_iterable(self):
        """
        if 'start' points beyond the end of the iterable, then my_islice instance should be already a consumed generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        start = len(iterable) + 1
        stop = start + 1
        step = 1
        reference_iterator = islice(iterable, start, stop, step)
        under_test_generator = my_islice(iterable, start, stop, step)
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_start_pointing_the_end_of_iterable(self):
        """
        if 'start' points at the end of the iterable, then my_islice instance should be returning the last item
        in the iterable
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        start = len(iterable) - 1  # start = 9, pointing at 10
        stop = start + 1
        step = 1
        reference_iterator = islice(iterable, start, stop, step)
        under_test_generator = my_islice(iterable, start, stop, step)
        # print(list(reference_iterator))
        # print(list(under_test_generator))
        self.assertEqual(list(reference_iterator), list(under_test_generator))

    def test_start_stop_step_are_None(self):
        """
        my_islice(iterable, start, stop[, step]) --> my_islice generator
        """
        iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        reference_iterator = islice(iterable, None, None, None)
        under_test_generator = my_islice(iterable, None, None, None)
        self.assertEqual(list(reference_iterator), list(under_test_generator))


if __name__ == '__main__':
    unittest.main()
