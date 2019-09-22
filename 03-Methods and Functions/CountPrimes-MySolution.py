import math


def is_prime(num):
    """
    returns True if num is prime. Returns False otherwise
     Note that by convention 0 and 1 are not prime
    """
    if num == 0 or num == 1:  # By convention, 0 and 1 are not prime
        return False
    if num % 2 == 0 and num > 2:  # for 4, 6, 8, 10, 12, ...
        return False
    # At this point, we know that num is NOT range(4,inf,2) nor it is 0 or 1
    # the possible num values are 2,3,5,7,9,11 and so forth
    for i in range(3, int(math.sqrt(num)) + 1, 2):   # for num = 9, 11, 13, ... returns a non-empty range
        if num % i == 0:
            return False  # for 9, 15
    return True  # for num = 2, 3, 5, 7, 11, 13, ...


# num must be greater than or equal to zero
def count_primes(num):
    lst = list(range(0, num+1))  # create a list from 0 (inclusive) to num (inclusive)
    prime_numbers_lst = list(filter(is_prime, lst))
    return len(prime_numbers_lst)


print(f'count_primes(100): {count_primes(100)}')