#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:24:30 2020
This function request the user to enter a name and 4 separate numbers. 
The function then computes the sum of all 4 numbers and displays the result
@author: gavita
"""

def sumNumbers():
    
    # Get the user's name 
    name = input("What is your name? Enter your name: ")
    
        # Get the user for their 4 numbers and convert to integer
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))
    num4 = int(input("Enter your fourth number: "))

    # Add the numbers
    sumNum = num1 + num2 + num3 + num4
    
    # Display the sum
    print("Hi " + name + ". The total sum of the numbers are " + str(sumNum))

               