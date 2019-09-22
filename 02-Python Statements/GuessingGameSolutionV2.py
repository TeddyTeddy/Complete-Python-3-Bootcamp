from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

number = randint(1, 100)
print(f'number is {number}')
lower_end = number - 10 if number - 10 >= 1 else 1
higher_end = number + 10 if number + 10 <= 100 else 100
warm_range = list(range(lower_end, higher_end + 1))
print('warm range:', warm_range)
guessed_numbers = []

while True:
    guess = int(input('Enter your guess: '))
    is_guess_out_of_range = guess > 100 or guess < 1
    while is_guess_out_of_range:
        print('OUT OF BOUNDS!')
        guess = int(input('Enter your guess: '))
        is_guess_out_of_range = guess > 100 or guess < 1
    # a valid guess is entered
    guessed_numbers.append(guess)
    if guessed_numbers[-1] == number:
        print(f'Guess {number} right at {len(guessed_numbers)} iterations')
        break  # stops program
    # if execution reaches here, number is not guessed yet
    if len(guessed_numbers) == 1:  # is it the first iteration?
        if guessed_numbers[-1] in warm_range:  # is the guessed number in warm range?
            print('WARM!')
        else:
            print('COLD!')
    else:  # subsequent rounds than the first round
        if(abs(guessed_numbers[-1]-number)) < abs(guessed_numbers[-2]-number):  # if the distance is getting better
            print('WARMER!')
        else:
            print('COLDER!')
