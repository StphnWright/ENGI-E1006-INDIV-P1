**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

**Take-home project 1**

Due: Wednesday February 10 11:59pm, New York time (ET / GMT-5)
Total Points: 100

The code you submit for take-home projects must be your own work. Please review the academic honesty
policy for this course (at the end of the syllabus page). You are however welcome to discuss the problem
in general terms with other students as long as you don't discuss or exchange your code.

Do not use Python modules other than those explicitly mentioned. 

Upload the following two files to Courseworks:

	part1.py 
	part2.py

Important: If you re-submit your assignment you need to re-upload all files, even if you changed just one
of them. Otherwise, any files you uploaded previously will be lost if you submit a second time.
 

**Part 1 - Guessing Game (50 pts) **

In this problem you will implement a simple guessing game.

First, the program should choose a secret number x between 1 and 10. Use the random function in the random
module (random.random()) to pick a random number, as illustrated in class. 

Then, the program should prompt the user to type in a number. If the player guesses x correctly, the program
should print a message and terminate.

Otherwise, the program should print a hint and then ask the user for another guess: 

	• if the difference between x and the guess is greater than 5, the program prints ‘not even close’.
	• if the difference between x and the guess is between 3 and 5 (inclusive), the program prints ‘close’.
	• if the difference between x and the guess is less than 3, the program prints ‘almost there’.

The program should repeat asking the user for another input until the user guesses correctly or until there were
five incorrect guesses. The program should keep track of the number of guesses. If the user cannot guess x in their
fifth guess, the program informs her that the game is lost and quits.

Your program should be in a single file part1.py.  Make sure to convert the user input into an int. Use a loop
to ask for guesses and print hints repeatedly.

**Part 2 - Inverse guessing game (50 pts)** 

Let’s inverse the roles in the guessing game. This time, the player chooses a secret number between 1 and 10
(in their mind) that the computer must guess. For this purpose, the computer suggests a number and the player
indicates if it is 1) too big, 2) too small or 3) correct. The player's response should be read as user input.
If the number is correct, the program should terminate. Otherwise the computer will ask another number repeatedly.
The computer only has three attempts to guess the right number.

Write the inverse guessing game as a new Python program in the file part2.py. Before starting to program, make sure
to plan out your algorithm (maybe on paper).

The strategy the compute should follow is similar to Binary Search. This is a requirement. It's okay if the computer
always guesses 5 as the first number although that will make some numbers "unreachable". You may also select a random
number as the first number, but you should still use the steps of Binary Search to guess the next numbers.
