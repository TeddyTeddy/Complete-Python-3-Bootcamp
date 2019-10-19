

# implemented a built-in equivalent of iter() function
# behind the scenes, my_iter stores its own symbol table (i.e. its state via locals())
# and the line number where execution should be resumed. Next time the iterator is invoked
# execution starts from the line number along with the stored symbol table.
def my_iter(iterable):
    for item in iterable:
        yield item


if __name__ == '__main__':
    s = 'Hello'  # string is an iterable
    s_iter = my_iter(s)  # note that there is no "next(my_iter(s))" here, it just returns an iterator object
    print(s_iter)        # <generator object my_iter at 0x7f30b124d360>

    print('(1) For loop calling on iterator s_iter')
    # for loop implementation (1) and while loop implementation (2) are equivalent
    # (1) For loop calling on iterator s_iter
    for letter in s_iter:  # keep invoking s_iter iterator till it raises StopIteration
        print(letter)
    # once the for loop is over, s_iter iterator is in a state, where next(s_iter) would raise StopIteration
    # print(next(s_iter))  ## uncomment this line and see StopIteration error for yourself

    print("(2) While loop calling on next(s_iter)")
    # (2) While loop calling on next(s_iter)
    s_iter = my_iter(s)    # re-initialize s_iter with a brand new iterator object with its zeroed state
    print(s_iter)       # <generator object my_iter at 0x7fdb0ae03ba0>
    while True:
        try:
            letter = next(s_iter)
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

