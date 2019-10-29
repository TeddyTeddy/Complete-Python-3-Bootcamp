

# def zip(__iter1: Iterable,
#         __iter2: Iterable,
#         __iter3: Iterable,
#         __iter4: Iterable,
#         __iter5: Iterable,
#         __iter6: Iterable,
#         *iterables: Iterable) -> Iterator[Tuple[Any, ...]]
# Possible types:
# • (__iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]
# • (__iter1: Iterable[_T1], __iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]
# • (__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]
# • (__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]
# • (__iter1: Iterable[_T1], __iter2: Iterable[_T2], __iter3: Iterable[_T3], __iter4: Iterable[_T4], __iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]
# • (__iter1: Iterable, __iter2: Iterable, __iter3: Iterable, __iter4: Iterable, __iter5: Iterable, __iter6: Iterable, iterables: Tuple[Iterable, ...]) -> Iterator[Tuple[Any, ...]]
# zip(iter1 [,iter2 [...]]) –> zip object
# Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the iterables.
# The .__next__() method continues until the shortest iterable in the argument sequence
# is exhausted and then it raises StopIteration. With no arguments, it returns an empty iterator.
def my_zip(*iterables):
    if len(iterables) != 0:  # if not zero, returns an empty iterator
        # get iterators from iterables
        iterators = [iter(iterable) for iterable in iterables]
        while True:
            try:
                i_th = []
                for iterator in iterators:
                    i_th.append(next(iterator))  # can throw StopIteration error
            except StopIteration: # shortest iterator raised StopIteration error
                break
            else:  # did not raise StopIteration error
                yield tuple(i_th)


# the same implementation in a class form (as in builtin class zip)
class MyZip:
    def __init__(self, *iterables):
        self._iterators = [iter(iterable) for iterable in iterables]  # can be an empty list if no iterables

    def __iter__(self):
        return self    # returns itself as its own iterator

    def __next__(self):
        if not self._iterators:
            raise StopIteration

        i_th = []
        for iterator in self._iterators:
            i_th.append(next(iterator))  # can throw StopIteration error

        return tuple(i_th)

