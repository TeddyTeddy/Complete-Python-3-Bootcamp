# TASK
# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


def up_low(str):

    number_of_lower = 0
    number_of_upper = 0
    for char in str:
        if char.isalpha():
            if char.islower():
                number_of_lower += 1
            else:
                number_of_upper += 1

    print(f'Original String : {str}')
    print(f'No. of Upper case characters : {number_of_upper}')
    print(f'No. of Upper case characters : {number_of_lower}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)