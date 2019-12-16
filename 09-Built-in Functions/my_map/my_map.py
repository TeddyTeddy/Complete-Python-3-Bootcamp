def get_total(*args):
    # print(f'inside get_total() and *args are: {args}')
    for arg in args:
        if type(arg) != int:
            msg = f'Expected int argument, got {type(arg)} argument'
            raise TypeError(msg)
    return sum(args)


def my_map(*args):
    """
    def map(__func: (...) -> _S,
            __iter1: Iterable,
            __iter2: Iterable,
            __iter3: Iterable,
            __iter4: Iterable,
            __iter5: Iterable,
            __iter6: Iterable,
            *iterables: Iterable) -> Iterator[_S]
    Possible types:
    • (__func: (_T1) -> _S, __iter1: Iterable[_T1]) -> Iterator[_S]
    • (__func: (_T1, _T2) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> Iterator[_S]
    • (__func: (_T1, _T2, _T3) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> Iterator[_S]
    • (__func: (_T1, _T2, _T3, _T4) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]) -> Iterator[_S]
    • (__func: (_T1, _T2, _T3, _T4, _T5) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> Iterator[_S]
    • (__func: (...) -> _S, __iter1: Iterable, __iter2: Iterable, __iter3: Iterable, __iter4: Iterable, __iter5: Iterable, __iter6: Iterable, iterables: Tuple[Iterable, ...]) -> Iterator[_S]
    map(func, *iterables) –> map object
    Make an iterator that computes the function using arguments from each of the iterables.
    Stops when the shortest iterable is exhausted.
    """
    if len(args) < 2:
        msg = f'my_map must have at least two arguments.'
        raise TypeError(msg)

    func = args[0]
    if not callable(func):
        msg = f'{type(func)} object is not callable'
        raise TypeError(msg)

    iterables = list(args)
    iterables.pop(0)  # remove func, we are left with iterables
    for i in iterables:
        if '__iter__' not in dir(i):  # check if every iterable i is indeed iterable
            msg = f'{type(func)} object is not iterable'
            raise TypeError(msg)

    # at this point: func is callable an all iterables are indeed iterables
    iterators = [iter(i) for i in iterables]

    while True:
        try:
            arguments = []
            for iterator in iterators:
                arguments.append(next(iterator))  # can raise StopIteration error
        except StopIteration:
            return  # In a generator function, the return statement indicates that the generator is done and
            # will cause StopIteration to be raised.
        else:
            yield func(*arguments)


if __name__ == '__main__':
    list_1 = [1, 2, 3]  # an iterable
    list_2 = [5, 2, 4]  # an iterable
    list_3 = [7, 7, 7]  # an iterable

    # USING A FUNCTION (i.e. get_total)
    builtin_map_instance = map(get_total, list_1, list_2, list_3)     # built-in map class usage, returns an iterator
    print('__next__' in dir(builtin_map_instance))  # True, built-in map returns a generator, which is an iterator
    print('__iter__' in dir(builtin_map_instance))  # True, built-in map iterator is an iterable
    print(builtin_map_instance == iter(builtin_map_instance))  # True, map instance returns itself as iterator
    print(list(builtin_map_instance))

    my_map_generator = my_map(get_total, list_1, list_2, list_3)  # own my_map usage
    print('__next__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterator
    print('__iter__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterable
    print(my_map_generator == iter(my_map_generator))  # True, proof that my_map returns itself as its own iterator
    print(list(my_map_generator))  # Yes! list class excepts our own "my_map" iterator

    # USING LAMBDA EXPRESSION instead of get_total
    builtin_map_instance = map(lambda x, y, z: x+y+z, list_1, list_2, list_3)  # built-in map class usage, returns an iterator
    print('__next__' in dir(builtin_map_instance))  # True, built-in map returns a generator, which is an iterator
    print('__iter__' in dir(builtin_map_instance))  # True, built-in map iterator is an iterable
    print(builtin_map_instance == iter(builtin_map_instance)) # True, map instance returns itself as iterator
    print(list(builtin_map_instance))

    my_map_generator = my_map(lambda x, y, z: x+y+z, list_1, list_2, list_3)  # own my_map usage
    print('__next__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterator
    print('__iter__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterable
    print(my_map_generator == iter(my_map_generator))  # True, proof that my_map returns itself as its own iterator
    print(list(my_map_generator))  # Yes! list class excepts our own "my_map" iterator
