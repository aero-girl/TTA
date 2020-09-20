# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 4:Replace all odd numbers in the above array with 1 
(this means by subtract by 1)
@author: Gavi
"""

import numpy as np

# Create a 1D array of numbers from 1 to 10
array3 = np.arange(1,10)

# Extract all odd numbers from array of 1 10 and substitute with -1
print('1D array of numbers from 1 to 10:',array3)
# If a number divided by 2 has a remainder than it is an even number
array3[array3 % 2 == 1] = -1
print('Odd numbers substituted with -1:',array3)




