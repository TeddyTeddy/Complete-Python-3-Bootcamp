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
    iterables = list(args)
    iterables.pop(0)  # 0.th argument is a function, not an iterable
    iterators = []
    for iterable in iterables:
        iterators.append(iter(iterable))

    while True:
        try:
            arguments = []
            for iterator in iterators:
                arguments.append(next(iterator))  # next(i) can throw a StopIteration error
        except StopIteration:
            break
        else:  # no StopIteration error
            yield func(*arguments)


if __name__ == '__main__':
    list_1 = [1, 2, 3]  # an iterable
    list_2 = [5, 2, 4]  # an iterable
    list_3 = [7, 7, 7]  # an iterable
    gen_total_iterator1 = map(get_total, list_1, list_2, list_3)     # built-in map usage
    get_total_iterator2 = my_map(get_total, list_1, list_2, list_3)  # own my_map usage

    # get_total_iterator is an iterable, which returns itself as its own iterator
    print('__iter__' in dir(get_total_iterator2))  # True, proof that get_total_iterator2 is an iterable
    iterator1 = iter(get_total_iterator2)
    iterator2 = iter(iterator1)
    print(iterator1 == iterator2)  # True, proof that get_total_iterator returns itself as iterator

    print(list(get_total_iterator2))  # Yehuu! list class excepts our own "my_map" iterator
    print(list(gen_total_iterator1))
