from itertools import islice
import math

def my_islice(*args):
    """
    my_islice(iterable, stop) --> my_islice generator
    my_islice(iterable, start, stop[, step]) --> my_islice generator

    Return an iterator whose next() method returns selected values from an
    iterable.  If start is specified, will skip all preceding elements;
    otherwise, start defaults to zero.  Step defaults to one.  If
    specified as another value, step determines how many values are
    skipped between successive calls.  Works like a slice() on a list
    but returns an iterator.
    """
    if len(args) < 2:
        msg = f'my_islice expected at least 2 arguments, got {len(args)}'
        raise TypeError(msg)
    if len(args) > 4:
        msg = f'my_islice expected at most 4 arguments, got {len(args)}'
        raise TypeError(msg)

    if '__iter__' not in dir(args[0]):
        msg = f'{type(args[0])} object is not iterable'
        raise TypeError(msg)

    start = 0
    step = 1
    stop = None
    iterable = args[0]
    if len(args) == 2:
        stop = args[1]
    elif len(args) == 3:
        start = args[1]
        stop = args[2]
    elif len(args) == 4:
        start = args[1]
        stop = args[2]
        step = args[3]

    if type(stop) != int and stop is not None:
        msg = f'Stop argument for my_islice() must be None or an integer: 0 <= x <= sys.maxsize.'
        raise ValueError(msg)

    if (type(start) != int and start is not None) or (type(start) == int and start < 0):
        msg = f'Indices for my_islice() must be None or an integer: 0 <= x <= sys.maxsize'
        raise ValueError(msg)

    if (type(step) != int and step is not None) or (type(step) == int and step <= 0):
        msg = f'Step for my_islice() must be a positive integer or None.'
        raise ValueError(msg)

    start = 0 if start is None else start
    stop = math.inf if stop is None else stop
    step = 1 if step is None else step

    iterator = iter(iterable)
    if start > 0:  # If start is specified, will skip all the preceding elements
        current = 0
        while current < start:
            try:
                # Important! for some reason, when StopIteration is raised directly via next()
                # call we need to trap it and then call return. Then the generator will not crash
                # with StopIteration exception.
                next(iterator)  # ignore the preceding element before start, can raise StopIteration error
            except StopIteration:
                return  # In a generator function, the return statement indicates that the generator is done and
                # will cause StopIteration to be raised.
            else:
                current += 1

    while start < stop:
        try:
            # important! for some reason, "yield next(iterator)" cannot be used together
            # when next(iterator) raises StopIteration error, the generator stops running
            value = next(iterator)    # can raise StopIteration
        except StopIteration:
            break  # the while loop
        else:
            yield value
            if step > 1:            # ignore elements in between steps
                ignore = 1
                while ignore < step:
                    next(iterator)  # ignore any element in between steps
                    ignore += 1
            start += step


# a generator function that yields an infinite sequence
def fibonacci():
    previous, current = 0, 1
    while True:
        yield current
        previous, current = current, previous + current


if __name__ == '__main__':

    fb_generator = my_islice(fibonacci(), 3, 7)
    print(list(fb_generator))

