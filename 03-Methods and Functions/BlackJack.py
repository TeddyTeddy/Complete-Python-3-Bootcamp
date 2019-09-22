# TASK
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
# blackjack(7,7,7) --> 21


def is_valid(x):
    if 1 <= x <= 11:
        return True
    return False


def blackjack(a,b,c):
    if is_valid(a) and is_valid(b) and is_valid(c):
        total = a + b + c
        if total <= 21:
            return total
        elif a == 11 or b == 11 or c == 11:   # sum exceeds 21 and there is an eleven in a, b, c
            total -= 10

        if total > 21:
            return 'BUST'
        else:
            return total
    else:
        return 'invalid argument(s)'


print(f'blackjack(5,6,7): {blackjack(5,6,7)}')
print(f'blackjack(9,9,9): {blackjack(9,9,9)}')
print(f'blackjack(9,9,11): {blackjack(9,9,11)}')
print(f'blackjack(7,7,7): {blackjack(7,7,7)}')
