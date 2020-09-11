# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:39:26 2020
Write a program that asks a user for their favourite number and then tells 
them a joke.  The program will call a joke printing function with the users 
favourite number.
@author: Gavi
"""


# Define range of numbers from 0 to 10 in increments of 1
numberList = [*range(1, 6, 1)] 
  
#Initialise number
number = 10

while True:
    
    if number < numberList[0] or number > numberList[-1]:
        print("Sorry number not in range, please try again")
    # Get a favourite number from a user
        number = int(input("Enter your favourite number ranging from 1-5 : "))
    elif number == 1 :
        print("\nWhy do we tell actors to “break a leg?\n")
        print("Because every play has a cast.")
        break
    elif number == 2 :
       print("\nHelvetica and Times New Roman walk into a bar\n")
       print("Get out of here!” shouts the bartender. “We don’t serve your type.")
       break
    elif number == 3 :
       print("\nWhy don’t scientists trust atoms?\n")
       print("Because they make up everything.")
       break
    elif number == 4 :
       print("\nHear about the new restaurant called Karma?\n")
       print("There’s no menu. You get what you deserve.")
       break
    elif number == 5 :
       print("\nDid you hear about the claustrophobic astronaut?\n")
       print("He just needed a little space.")
       break