import random

chances = 0
num = random.randint(1,9)
while chances < 5:
    guess = int(input('Enter your number: \t'))
    if guess > num:
        print(f'Guess a lower number than {guess}')
    elif guess < num:
        print(f'Guess a higher number than {guess}')
    else:
        print('Congratulation! you won')
        break
    chances = chances + 1
if chances > 5:
    print('You lose. Try next time')