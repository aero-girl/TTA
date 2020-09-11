# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 19:53:28 2020

@author: Gavi
"""

import random
print("Hello! What is your name?")
myName = input()
number = random.randint(1, 10)

print("Well, " + myName + ", I am thinking of a number between 1 and 10.")
print("Take a guess. The clue is: " + str(number))
# Initialise NuGuess to be 0
NuGuess = 0

# while NuGuess is greater than 0
while NuGuess > 0:
    
    guess = int(input("Take a guess"))
        
    # display NuGuess
    print("Number of Guesses = " + NuGuess)
    
    if guess == number:
        print("Good job, " + myName + "! You guessed my number")
    elif guess != number:
        print("Oooops! bad guess " + myName + "! Try again?!")

    # Add 1 to NuGuess
        NuGuess += 1