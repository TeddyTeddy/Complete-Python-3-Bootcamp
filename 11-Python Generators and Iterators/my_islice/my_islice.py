# a generator function that yields an infinite sequence
def fibonacci():
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current

# my_islice(iterable, stop) –> islice object
# my_islice(iterable, start, stop[, step]) –> islice object
# Return an iterator whose next() method returns selected values
# from an iterable. If start is specified, will skip all preceding elements;
# otherwise, start defaults to zero. Step defaults to one.
# If specified as another value, step determines how many values are
# skipped between successive calls. Works like a slice() on a list but
# returns an iterator.
def my_islice(*args):

    if len(args) < 2:
        msg = f'my_islice expected at least 2 arguments, got {len(args)}'
        raise TypeError(msg)
    if len(args) > 4:
        msg = f'my_islice expected at most 4 arguments, got {len(args)}'
        raise TypeError(msg)

    step = 1
    start = 0
    if len(args) == 2:
        iterable = args[0]
        stop = args[1]
    elif len(args) == 3:
        iterable = args[0]
        start = args[1]
        stop = args[2]
    elif len(args) == 4:
        iterable = args[0]
        start = args[1]
        stop = args[2]
        step = args[3]

    # verifications can be implemented for the values iterable,
    # start, stop and step here
    # but we assume they are fine

    current = start
    iterator = iter(iterable)
    while current < stop:
        yield next(iterator)
        current += step


if __name__ == '__main__':
    generator = fibonacci()
    lst = list(my_islice(generator, 0, 10))
    print(lst)
