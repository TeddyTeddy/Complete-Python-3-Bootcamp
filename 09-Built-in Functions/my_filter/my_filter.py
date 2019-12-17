class MyFilter(object):
    """
    @overload def filter(__function: (_T) -> Any,
               __iterable: Iterable[_T]) -> Iterator[_T]
    Possible types:
    • (__function: None, __iterable: Iterable[Optional[_T]]) -> Iterator[_T]
    • (__function: (_T) -> Any, __iterable: Iterable[_T]) -> Iterator[_T]

    MyFilter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    def __init__(self, func, iterable):
        if not hasattr(iterable, '__iter__'):
            raise TypeError(f'{type(iterable)} object is not iterable')

        self._func = func
        self._iterator = iter(iterable)

    def __iter__(self):
        return self     # MyFilter is an iterable and its own iterator

    def __next__(self):
        if self._func is not None and not callable(self._func):
            raise TypeError(f'{type(self._func)} object is not callable')

        if self._func is None:  # If function is None, return the items that are true
            while True:
                item = next(self._iterator)  # can raise StopIteration error
                if item:
                    return item
        else:  # function is not None
            while True:
                item = next(self._iterator)  # can raise StopIteration error
                if self._func(item):
                    return item


if __name__ == '__main__':

    range_iterable = range(20)  # range class instance, which is an iterable
    # utilizing built-in filter class passing a lambda expression
    filter_iterable = filter(lambda x: x % 2 == 0, range_iterable)  # filter class instance, which is an iterable
    print(hasattr(filter_iterable, '__iter__'))  # True, filter_iterable is indeed an iterable
    print(hasattr(filter_iterable, '__next__'))  # True, filter_iterable is an iterator
    lst = list(filter_iterable)  # populate list container
    print(lst)

    # utilizing MyFilter implementation passing a lambda expression
    my_filter_iterable = MyFilter(lambda x: x % 2 == 0, range_iterable)
    print(hasattr(my_filter_iterable, '__iter__'))  # True, my_filter_iterable is an iterable
    print(hasattr(my_filter_iterable, '__next__'))  # True, my_filter iterable is an iterator
    lst = list(my_filter_iterable)  # Yes, list class accepts MyFilter instance as iterable
    print(lst)

    # utilizing built-in filter class passing None as a function
    filter_iterable = filter(None, range_iterable)  # filter class instance, which is an iterable
    print(hasattr(filter_iterable, '__iter__'))  # True, filter_iterable is indeed an iterable
    print(hasattr(filter_iterable, '__next__'))  # True, filter_iterable is an iterator
    lst = list(filter_iterable)  # populate list container
    print(lst)

    # utilizing MyFilter implementation passing None as a function
    my_filter_iterable = MyFilter(None, range_iterable)
    print(hasattr(my_filter_iterable, '__iter__'))  # True, my_filter_iterable is an iterable
    print(hasattr(my_filter_iterable, '__next__'))  # True, my_filter iterable is an iterator
    lst = list(my_filter_iterable)  # Yes, list class accepts MyFilter instance as iterable
    print(lst)
