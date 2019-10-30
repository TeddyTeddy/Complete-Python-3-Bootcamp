

# Refer to unit tests for my_range() function
# NOTE! built-in range is a CLASS implementing __iter__(),  which makes it an iterable.
# Below, we implement a generator function to mimic the behaviour of built in range class
# From range documentation:
# Possible types:
# • (self: range, stop: int) -> None
# • (self: range, start: int, stop: int, step: int) -> None
#
#  range(stop) -> range object range(start, stop[, step]) -> range object
#  Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
#  range(i, j) produces i, i+1, i+2, ..., j-1. start defaults to 0, and stop is omitted!
#  range(4) produces 0, 1, 2, 3. These are exactly the valid indices for a list of 4 elements.
#  When step is given, it specifies the increment (or decrement).
def my_range(*args):
    """
    A built-in range() function equivalent, an iterator function
    :param args:  A variable length of arguments
    :return: a generator
    """
    # check if correct number of arguments are given
    if len(args) < 1:
        msg = f'range expected 1 arguments, got {len(args)}'
        raise TypeError(msg)
    if len(args) > 3:
        msg = f'range expected at most 3 arguments, got {len(args)}'
        raise TypeError(msg)

    # number of args is between 1 to 3. Fine.
    # now check the type of args. They all have to be int
    for arg in args:
        if type(arg) != int:
            msg = f'{type(arg)} object cannot be interpreted as an integer'
            raise TypeError(msg)

    # both number of args and type of args are correct
    # start initializing start, stop, step variables
    start = 0
    step = 1
    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]

    # start, stop, and step got initialized
    if step > 0:
        current = start
        while current < stop:
            yield current
            current += step
    else:  # step is negative, it specifies a decrement
        current = start
        while current > stop:
            yield current
            current += step


class MyRangeIterator:
    def __init__(self, start, stop, step):
        self._start = start
        self._stop = stop
        self._step = step
        self._current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._step > 0:  # step is positive, it specifies an increment
            if self._current < self._stop:
                self._current += self._step
                return self._current - self._step  # return the previous self._current
            else:
                raise StopIteration
        else:  # step is negative, it specifies a decrement
            if self._current > self._stop:
                self._current += self._step
                return self._current - self._step  # return the previous self._current
            else:
                raise StopIteration


# A -partial- implementation of built-in class range()
# If you check builtin range class, you will see many more methods to be implemented
class MyRange:
    def __init__(self, *args):
        """
        A built-in range() function equivalent, an iterator function
        :param args:  A variable length of arguments
        :return: a generator
        """
        # check if correct number of arguments are given
        if len(args) < 1:
            msg = f'range expected 1 arguments, got {len(args)}'
            raise TypeError(msg)
        if len(args) > 3:
            msg = f'range expected at most 3 arguments, got {len(args)}'
            raise TypeError(msg)

        # number of args is between 1 to 3. Fine.
        # now check the type of args. They all have to be int
        for arg in args:
            if type(arg) != int:
                msg = f'{type(arg)} object cannot be interpreted as an integer'
                raise TypeError(msg)

        # both number of args and type of args are correct
        # start initializing start, stop, step variables
        self._start = 0
        self._step = 1
        if len(args) == 1:
            self._stop = args[0]
        elif len(args) == 2:
            self._start = args[0]
            self._stop = args[1]
        elif len(args) == 3:
            self._start = args[0]
            self._stop = args[1]
            self._step = args[2]

    def __iter__(self):
        return MyRangeIterator(self._start, self._stop, self._step)


