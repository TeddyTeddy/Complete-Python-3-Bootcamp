import my_range


def gensquares(n):
    """
    a generator that generates the squares of numbers up to some number N.
    :param N:
    :return:
    """
    for number in my_range.my_range(n):  # note that we are NOT calling range(N), we implemented our own my_range() generator
        yield number**2


if __name__ == '__main__':
    print('Calling iterator gensquares(10) in a for loop')
    for x in gensquares(10):  # gensquares(10) is a generator throwing StopIteration when exhausted
        print(x)

