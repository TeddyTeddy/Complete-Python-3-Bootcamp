from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

number = randint(1, 100)
min_number = number - 10 if number - 10 >= 1 else 1
max_number = number + 10 if number + 10 <= 100 else 100
warm_range = list(range(min_number, max_number+1))
print(f'number: {number}')
print(f'warm_range: {warm_range}')

guessed_numbers = []
while True:
    guess = int(input('Enter your guess:'))
    if guess < 1 or guess > 100:
        print('Out of bounds!')
        continue

    # guess is in range 1 to 100
    guessed_numbers.append(guess)
    if guessed_numbers[-1] == number:  # number is guessed right
        print(f'You guessed {number} right in {len(guessed_numbers)} iteration(s)')
        break

    # number is not guessed right
    if len(guessed_numbers) == 1:  # if it is in the first guess
        if guess in warm_range:
            print('Warm!')
        else:
            print('Cold')
    else: # if the second, third, ... n.th guess
        if abs(guessed_numbers[-1] - number) < abs(guessed_numbers[-2] - number):
            print('Warmer!')
        else:
            print('Colder!')


