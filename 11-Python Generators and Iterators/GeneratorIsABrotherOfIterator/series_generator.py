# With iterators, you need to implement a class that has __iter__() and __next__() methods
class Series(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # the iteration protocol method
    def __iter__(self):
        return self     # iterable object is the iterator itself in this case

    # the iteration protocol method
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


# The generator is the elegant brother of iterator that allows you to write iterables like the one you saw earlier,
# but in a much easier syntax where you do not have to write classes with __iter__() and __next__() methods.
# The magic word with generators is yield. There is no return statement in the function series_generator.
# The return value of the function will actually be a generator
def series_generator(low, high):
    while low <= high:
        yield low
        low += 1
    pass  # the last line of the code, if an iteration reaches this point, Python raises StopIteration


if __name__ == '__main__':
    # (A)s
    n_list = Series(1, 10)   # an iterable object that returns an iterator when __iter__() method called
    print(list(n_list))      # you can cast an iterable into a list()

    # (1) and (2) are equivalent to each other and they implement (A) utilizing generators
    # (1) populating a series, which is a container in memory
    n_list = []
    for num in series_generator(1, 10):
        n_list.append(num)
    print(n_list)

    # (2): How Python runs (1) in the background
    n_list = []
    generator = series_generator(1, 10)  # this is not a fn call! It returns a generator object
    print(generator)
    while True:
        try:
            # Inside the while loop when the execution reaches the yield statement,
            # the value of low is returned and the generator state is suspended (i.e. state suspension)
            num = next(generator)  # a generator object is an iterator object
        except StopIteration:
            break
        else:  # there was not any StopIteration exception
            n_list.append(num)
    print(n_list)




