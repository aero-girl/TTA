# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:53:28 2020
Practical to extend the Guessing Game
1. Give the user 6 chances to guess the number use
2. Let them know if their guess is too high
3. Let them know if their guess is too low
@author: Gavi
"""

import random
print("Hello! What is your name?")
myName = input()
number = random.randint(1, 10)

# Display text
print("Well, " + myName + ", I am thinking of a number between 1 and 10.")
#print("Take a guess. The clue is: " + str(number))

# Initialise NuGuess to be 1
NuGuess = 1

# Define max guess to be 6
TotalNuGuess = 6

# while NuGuess is less than 6
while NuGuess < TotalNuGuess:
    
    # display NuGuess
    print("Number of Guess..." + str(NuGuess) +" out of " + str(6))
    
    # Store input as an integer within guess variable
    guess = int(input("Take a guess... :"))
        
    
    # If guess is correct, then break the loop
    if guess == number:
        print("Good job, " + myName + "! You guessed my number")
        break
    
    # Else if guess is less than the number, then display message and provide a hint
    elif guess < number:
        print("Oooops! bad guess " + myName + "! Your guess was to low.")
        print("Hint: Your guess was lower by " + str(number-guess))
        
    # Else if guess is more than the number, then display message and provide a hint
    elif guess > number:
        print("Oooops! bad guess " + myName + "! Your guess was to high.")
        print("Hint: Your guess was higher by " + str(guess-number))
        
        # Add 1 to NuGuess to increment it by 1
        NuGuess += 1