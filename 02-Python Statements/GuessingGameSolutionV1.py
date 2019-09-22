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
guess = int(input('Enter your guess: '))
guessed_numbers.append(guess)

if guess != number:
    if guess in warm_range:
        print('WARM!')
    else:
        print('COLD!')

while guessed_numbers[-1] != number:
    guess = int(input('Incorrect. Enter your next guess: '))
    guessed_numbers.append(guess)
    if guess != number:
        # if the guess is closer from the number than the previous guess
        if abs(guess - number) < abs(guessed_numbers[-2] - number):
            print('WARMER!')
        else:  # if the guess is further from the number than the previous guess
            print('COLDER!')
else:
    print(f'Guessed the number {guess} right in {len(guessed_numbers)} iterations')