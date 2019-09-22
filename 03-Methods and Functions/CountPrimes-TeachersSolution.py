def is_prime(x):
    """
    i.e. x = 9
    :param x: must be a number in a range starting from 3 and incremented by 2 (i.e. [3,5,7,9...]
    :return: True if x is prime, False otherwise
    """
    for y in range(3, x, 2):  # y in [3,5,7]
        if x % y == 0:        # 9 % 3 == 0
            return False      # for x = 9
    return True


def count_primes(num):
    """
    Returns the number of prime numbers up to and including the num itself
    :param num: a number up to which (inclusive) prime numbers will be listed
    :return: number of prime numbers from the range [0,num]
    """
    if num < 2:
        return 0   # by convention, 0 and 1 are not prime
    # num is >= 2 here
    primes = [2]
    counter = 3  # counter up to the input num
    while counter <= num:    # x in the range 3,5,7,9,11,13,15,...
        # is counter a prime number?
        if is_prime(counter):
            primes.append(counter)
        counter += 2  # 3,5,7,9,11 and so on
    print(f'primes: {primes}')
    return len(primes)


print(f'count_primes(100): {count_primes(100)}')
