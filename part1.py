"""
A program to play a number guessing game,
where the user guesses a secret number.

"""

import random

number = random.randint(1, 10) #generate random number
attempts = 1
max_attempts = 5

while attempts <= max_attempts:
    guess = int(input('Pick a number from 1 to 10: ')) #prompt user pick
    diff = abs(guess - number) #absolute value of guess minus secret number
    if diff == 0: #you guessed the correct number
        break #end game if correct
    elif diff > 5: #greater than 5
        print('Not even close...\n')
    elif diff >= 3: #3 or 4
        print('Close...\n')
    else: #2 or below
        print('Almost there...\n')
    attempts += 1 #try again if turns remain

if attempts > max_attempts: #if out of turns
    print('You lost - Game Over.')
else: #if correct
    print('You won!')
