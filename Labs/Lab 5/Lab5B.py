import random

num = random.randint(1, 50)

print('Try to guess the number that I am thinking of between 1 and 50.')
print('You have 5 chances to guess the number!')

i = 1

while i <= 5:
    print('Guess #{}: '.format(i), end='')
    guess = int(input())

    if guess < num:
        print('Too low. Try a higher number.')
    elif guess > num:
        print('Too high. Try a lower number.')
    else:
        print('Nice job! You guessed my secret number in', i, 'guesses!')
        break

    i += 1

if ((i == 6) and (guess != num)):
    print('Sorry, you have run out of guesses. The secret number was', num)
