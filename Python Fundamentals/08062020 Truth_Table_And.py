# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 13:00:38 2020
Get user to enter two input and evalute the AND result
@author: Gavi
"""


def get_user_input_boolean():
    #Get a boolean value from the user and return this value as a boolean.
    
    # Initialise user_input value
    user_input = "zzz"
    
    # Check if input is empty
    while user_input != "True" and user_input != "False":
        user_input = input ("Enter True or False:")
        

    # Set boolean value to the user input
        if user_input == "True" :
            user_input_boolean = True
        elif  user_input == "False" :
            user_input_boolean = False
        else:
            print("You entered " + user_input + ". Please enter True or False:")
            
    # Return the value
    return (user_input_boolean)

"""
a = get_user_input_boolean()
b = get_user_input_boolean()

# Print result of entered by user
print(str(a) + " AND " + str(b) + " is ...")

# Display the AND result
print (a and b)"""