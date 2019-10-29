

# implemented a built-in equivalent of iter() function
def my_iter(iterable):
    # check if iterable is indeed iterable
    if '__iter__' not in dir(iterable):
        iterable_type = type(iterable)
        msg = f' {iterable_type} object is not iterable'
        raise TypeError(msg)

    # if execution reaches here, then iterable is indeed iterable
    return iterable.__iter__()


if __name__ == '__main__':
    s = 'Hello'  # string is an iterable
    s_iterator = my_iter(s)  # note that there is no "next(my_iter(s))" here, it just returns an iterator object
    print(s_iterator)        # <str_iterator object at 0x7f18af85c978>

    print('(1) For loop calling on iterator s_iter')
    # for loop implementation (1) and while loop implementation (2) are equivalent
    # (1) For loop calling on iterator s_iter
    for letter in s_iterator:  # keep invoking s_iter iterator till it raises StopIteration
        print(letter)
    # once the for loop is over, s_iter iterator is in a state, where next(s_iter) would raise StopIteration
    # print(next(s_iter))  ## uncomment this line and see StopIteration error for yourself

    print("(2) While loop calling on next(s_iter)")
    # (2) While loop calling on next(s_iter)
    s_iterator = my_iter(s)    # re-initialize s_iter with a brand new iterator object with its zeroed state
    print(s_iterator)          # <str_iterator object at 0x7f18ada0b0f0>

    iterator = iter(s_iterator)  # s_iterator is iterable, and returns itself as own iterator
    while True:
        try:
            letter = next(iterator)
        except StopIteration:
            break
        else:
            print(letter)
    # print(next(s_iter))  ## uncomment this line and see StopIteration error for yourself

    print('Doing the above functionality with built-in iter() function')
    # Referring to above code, the usage of my_iter & for loop, lets use built-in iter() function instead
    s_iter = iter(s)
    print(s_iter)         # <str_iterator object at 0x7ff00f00cac8>
    for letter in s_iter:
        print(letter)


