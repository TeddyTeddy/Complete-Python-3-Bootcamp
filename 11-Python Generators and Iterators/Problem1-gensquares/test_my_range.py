import unittest
import my_range


def tuple_generator(file):
    for line in file:  # i.e. "3 7 2\n"
        line = line.replace('\n', '')       # remove "\n" from the line
        arguments_list = line.split(' ')    # i.e. ['3', '7', '2']
        arguments_list = [int(argument) for argument in arguments_list]  # i.e. [3, 7, 2]
        yield tuple(arguments_list)         # (3, 7, 2)


class TestMyRangeGeneratorFunction(unittest.TestCase):

    # https://stackoverflow.com/questions/17353213/init-for-unittest-testcase
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file = open('arguments.txt')
        self._tuple_generator = tuple_generator(self._file)

    def __del__(self):
        self._file.close()

    @staticmethod
    def populate_my_range_and_compare_with_builtin_range(self, *args):  # args i.e. (100, 2, -7)
        test_generator = my_range.my_range(*args)  # function to be tested
        verification_iterable = range(*args)       # to be verified against the built-in class
        self.assertEqual(list(test_generator), list(verification_iterable))

    def test_all_parameter_combos(self):
        for args in self._tuple_generator:  # args is a tuple i.e. (100, 2, -7)
            TestMyRangeGeneratorFunction.populate_my_range_and_compare_with_builtin_range(self, *args)


class TestMyRangeClass(unittest.TestCase):

    # https://stackoverflow.com/questions/17353213/init-for-unittest-testcase
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file = open('arguments.txt')
        self._tuple_generator = tuple_generator(self._file)
        # print(hasattr(self._tuple_generator, '__iter__'))  # True
        # print(hasattr(self._tuple_generator, '__next__'))  # True
        # print(self._tuple_generator == iter(self._tuple_generator))  # True

    def __del__(self):
        self._file.close()

    @staticmethod
    def instantiate_my_range_and_compare_with_range(self, *args):  # args i.e. (100, 2, -7)
        test_iterable = my_range.MyRange(*args)  # class to be tested
        verification_iterable = range(*args)     # to be verified against the built-in class
        self.assertEqual(list(test_iterable), list(verification_iterable))

    def test_all_parameter_combos(self):
        for args in self._tuple_generator:  # args is a tuple i.e. (100, 2, -7)
            TestMyRangeClass.instantiate_my_range_and_compare_with_range(self, *args)


if __name__ == '__main__':
    unittest.main()
