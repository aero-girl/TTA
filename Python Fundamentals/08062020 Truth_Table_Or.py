# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:00:38 2020
Get user to enter two input and evalute the AND or OR result, depending on 
user selection to use either the AND or OR table.
This function uses function previously defined within Truth_Table_And.py 
@author: Gavi
"""

# Importing  all the functions defined in Truth_Table_And.py 
from Truth_Table_And import *

# Get user input
a = get_user_input_boolean()
b = get_user_input_boolean()

# Initialise user_option value
user_option = "cat"
    
# Check if input is empty
while user_option != "AND" and user_option != "OR":
    user_option = input ("Enter AND or OR:")
    
    # Check is user_option  == "AND" and display Logical AND result
    if user_option  == "AND" :
        # Print result of entered by user
        print(str(a) + " AND " + str(b) + " is ...")

        # Display the AND result
        print (a and b)
    
    # Check is user_option  == "OR" and display Logical OR result
    elif  user_option == "OR" :
        # Print result of entered by user
        print(str(a) + " OR " + str(b) + " is ...")

        # Display the AND result
        print (a or b)
         
    else:
        print("You entere the following: " + user_option + ". Please enter either AND or OR:")   