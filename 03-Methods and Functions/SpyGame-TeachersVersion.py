# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1


print(f'spy_game([1,2,4,0,0,7,5]): {spy_game([1,2,4,0,0,7,5])}')
print(f'spy_game([1,0,2,4,0,5,7]): {spy_game([1,0,2,4,0,5,7])}')
print(f'spy_game([1,7,2,0,4,5,0]): {spy_game([1,7,2,0,4,5,0])}')




