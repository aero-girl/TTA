#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:26:42 2020
This function will get a user's name and number. It will then do some magic and 
display a number.
@author: gavita
"""

def name():
    age = 39
    month = 7
    
    # Get the user's name 
    name = input("What is your name? Enter your name:")
   
    # Get a number 
    number = int(input("Can you please enter a number ----> "))
    
    # Multiple by age and month
    finalNumber = number * age + month
    
    # Display result
    print("Hello " + (name))
    print("Your lucky number is " + str(finalNumber) + "!")