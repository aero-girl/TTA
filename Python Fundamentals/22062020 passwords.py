# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:11:24 2020
Create a program that asks the user to input a password, 
re enter the password and the tells the user if the password is weak, 
medium or strong.
@author: Gavi
"""

# Define infinite Loops
while True:
    # get input to password
    firstPassword = input("Please enter a password: ")
    secondPassword = input("please re-type your password: ")
    
    # Check if both entered passwords are the same
    if firstPassword == secondPassword:
        # Check length of passwords and inform user if password is strong, medium or weak
        if len(firstPassword) >12:
            print ("Your password is Strong")
            break
        elif len(firstPassword) > 6 and len(firstPassword) < 12:
            print ("Your password is Medium")
            break
        elif len(firstPassword) > 0 and len(firstPassword) < 6:
            print ("Your password is Weak")
            break
    else:
        print ("Password does not match. Please try again\n")
        
