"""
A program to play an inverse guessing game, 
where the computer guesses a secret number.

"""

import random
import time

lower = 1
upper = 10
attempts = 1
max_attempts = 3
guess = random.randint(lower,upper) #initial guess is random

print('Let\'s play a guessing game!\n')
time.sleep(1)
print('Think of a number between 1 and 10...')
time.sleep(2)
print('Then I get three tries to guess your secret number...')
time.sleep(2)
print('And you can tell me if my pick is Too Low, Too High, or Correct!\n')
time.sleep(3)
print('Ready? Here we go...')
time.sleep(2)

while attempts <= max_attempts:
    print('\nGuess #' + str(attempts) + ': ' + str(guess)) #guess secret number 
    hint = input('Is my guess Too Low, Too High, or Correct? ') #prompt hint
    if hint == 'Correct':
        break #end game if correct
    elif hint == 'Too Low':
        lower = guess + 1
        guess = (upper + guess) // 2
        attempts += 1
        if guess < lower:
          guess = lower
    elif hint == 'Too High':
        upper = guess - 1
        guess = (lower + guess) // 2
        attempts += 1
        if guess > upper:
          guess = upper
    elif attempts <= max_attempts: #data validation for invalid entry
      print('\nInvalid entry, please try again.')
    
if attempts > max_attempts: #if out of turns
    print('\nI couldn\'t guess your number - Player Wins!')
else: #if correct
    print('\nYour secret number is ' + str(guess) + ' - Computer Wins!')
