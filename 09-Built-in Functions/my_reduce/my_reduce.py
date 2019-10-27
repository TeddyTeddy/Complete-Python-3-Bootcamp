from functools import reduce


def add(a, b):
    return a + b


# Help on built-in function reduce in module functools:
#
# reduce(...)
#     reduce(function, sequence[, initial]) -> value
#
#     Apply a function of two arguments cumulatively to the items of a sequence,
#     from left to right, so as to reduce the sequence to a single value.
#     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
#     ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
#     of the sequence in the calculation, and serves as a default when the
#     sequence is empty.
def my_reduce(*args):
    if len(args) < 2 or len(args) > 3:
        msg = f'my_reduce expected at least 2 arguments, got {len(args)}'
        raise TypeError(msg)

    # TODO! check args[0] type must be a function

    # check args[1] type must be an iterable
    if '__iter__' not in dir(args[1]):
        msg = f'my_reduce() arg 2 must support iteration'
        raise TypeError(msg)

    # 2 or 3 args provided
    func = args[0]
    sequence = list(args[1])

    if len(args) == 3:
        initial = args[2]
        sequence.insert(0, initial)  # add initial to the beginning of the list 'sequence'

    # check if sequence has any value in it
    if len(sequence) == 0:
        msg = f'my_reduce() of empty sequence with no initial value'
        raise TypeError(msg)

    # sequence does contain at least 1 value
    sequence_iterator = iter(sequence)
    a = next(sequence_iterator)  # sequence has at least 1 value, cannot throw StopIteration
    try:
        b = next(sequence_iterator)
    except StopIteration:
        b = 0  # reduce(my_sum, [1]) returns 1

    result = func(a, b)
    for item in sequence_iterator:  # name item is an item from a sequence
        result = func(result, item)

    return result


if __name__ == '__main__':
    # call built-in reduce function
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    # call own my_reduce function
    print(my_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))

    # call built-in reduce function
    print(reduce(lambda x, y: x + y, {1, 2, 3}))
    # call own my_reduce function
    print(my_reduce(lambda x, y: x + y, {1, 2, 3}))
