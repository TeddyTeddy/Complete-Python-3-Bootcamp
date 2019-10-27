def get_total(*args):
    print(f'inside get_total() and *args are: {args}')
    for arg in args:
        if type(arg) != int:
            msg = f'Expected int argument, got {type(arg)} argument'
            raise TypeError(msg)
    return sum(args)


# def map(__func: (...) -> _S,
#         __iter1: Iterable,
#         __iter2: Iterable,
#         __iter3: Iterable,
#         __iter4: Iterable,
#         __iter5: Iterable,
#         __iter6: Iterable,
#         *iterables: Iterable) -> Iterator[_S]
# Possible types:
# • (__func: (_T1) -> _S, __iter1: Iterable[_T1]) -> Iterator[_S]
# • (__func: (_T1, _T2) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> Iterator[_S]
# • (__func: (_T1, _T2, _T3) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> Iterator[_S]
# • (__func: (_T1, _T2, _T3, _T4) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]) -> Iterator[_S]
# • (__func: (_T1, _T2, _T3, _T4, _T5) -> _S, __iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> Iterator[_S]
# • (__func: (...) -> _S, __iter1: Iterable, __iter2: Iterable, __iter3: Iterable, __iter4: Iterable, __iter5: Iterable, __iter6: Iterable, iterables: Tuple[Iterable, ...]) -> Iterator[_S]
# map(func, *iterables) –> map object
# Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted.
def my_map(*args):
    if len(args) < 2:
        msg = 'map() must have at least two arguments.'
        raise TypeError(msg)

    func = args[0]
    iterables_list = list(args)  # [function iterable1 iterable2 ...]
    iterables_list.pop(0)  # 0.th argument is a function, not an iterable --> [ iterable1, iterable2 ... ]
    iterators = []
    for iterable in iterables_list:
        iterators.append(iter(iterable))

    # iterator = iter(iterables_list)
    # while True:
    #     try:
    #         iterable = next(iterator)
    #     except StopIteration:
    #         break
    #     else:
    #         iterators.append(iter(iterable))

    while True:
        try:
            arguments = []
            for iterator in iterators:
                arguments.append(next(iterator))  # next(iterator) can throw a StopIteration error
        except StopIteration:
            break
        else:  # no StopIteration error
            yield func(*arguments)
    # raise StopIteration  ## imaginary statement for generator function my_map


if __name__ == '__main__':
    list_1 = [1, 2, 3]  # an iterable
    list_2 = [5, 2, 4]  # an iterable
    list_3 = [7, 7, 7]  # an iterable
    builtin_map_instance = map(get_total, list_1, list_2, list_3)     # built-in map class usage, returns an iterator
    print('__next__' in dir(builtin_map_instance))  # True, built-in map returns a generator, which is an iterator
    print('__iter__' in dir(builtin_map_instance))  # True, built-in map iterator is an iterable
    print(builtin_map_instance == iter(builtin_map_instance)) # True, map instance returns itself as iterator
    print(list(builtin_map_instance))

    my_map_generator = my_map(get_total, list_1, list_2, list_3)  # own my_map usage
    print('__next__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterator
    print('__iter__' in dir(my_map_generator))  # True, proof that my_map_generator is an iterable
    print(my_map_generator == iter(my_map_generator))  # True, proof that my_map returns itself as its own iterator
    print(list(my_map_generator))  # Yes! list class excepts our own "my_map" iterator

