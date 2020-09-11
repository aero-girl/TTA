#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:22:09 2020
Write a program which will ask for two numbers.
Then offers a menu to the user giving them a choice of operator
@author: gavita
"""

# Ask user for two numbers
number1 = int(input("Please enter your 1st number: "))
number2 = int(input("Please enter your 2nd number: "))
 
# Initialise menu = C
menu = "C"

# Start while loop
while menu != "A" or menu != "B" :
    
    # Display options to user
    menu = input(""" Please type in an option: \n
             Enter A for addition\n
             Enter B for multiplication\n""" )
    
    # If menu option chosen is A, then add numbers and print result
    if menu == "A":
        output = number1 + number2
        print("The sum of your numbers are " + str(output))
        break
    # If menu option chosen is B, then multiply numbers and print result
    elif menu == "B":
         output = number1 * number2
         print("The product of your numbers are " + str(output))
         break

