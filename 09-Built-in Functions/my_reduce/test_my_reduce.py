import unittest
from my_reduce import add
from my_reduce import my_reduce


class TestMyReduce(unittest.TestCase):
    def test_num_args_less_than_2(self):
        with self.assertRaises(TypeError):
            my_reduce()

        with self.assertRaises(TypeError):
            my_reduce(add)

    def test_num_args_greater_than_3(self):
        with self.assertRaises(TypeError):
            my_reduce(add, {1, 2, 3}, 5, 99)

        with self.assertRaises(TypeError):
            my_reduce(add, {1, 2, 3}, 5, 99, 33)

    def test_arg_two_must_support_iteration(self):
        does_not_support_iteration = 4
        with self.assertRaises(TypeError):
            my_reduce(add, does_not_support_iteration)

    def test_empty_sequence_provided(self):
        with self.assertRaises(TypeError):
            my_reduce(add, [])

    def test_no_function_provided(self):
        with self.assertRaises(TypeError):
            my_reduce(1, [1,2,3])

    def test_with_one_item_in_the_list(self):
        self.assertEqual(1, my_reduce(add, [1]))

    def test_with_list(self):
        sequence = [1, 2, 3]
        initial = 4
        self.assertEqual(my_reduce(add, sequence), 6)
        self.assertEqual(my_reduce(add, sequence, initial), 10)

    def test_with_set(self):
        sequence = {1, 2, 3, 4, 5}
        initial = 5
        self.assertEqual(my_reduce(add, sequence), 15)
        self.assertEqual(my_reduce(add, sequence, initial), 20)


if __name__ == '__main__':
    unittest.main()