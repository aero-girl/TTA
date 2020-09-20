# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 3: Extract all odd numbers from array of 1 10
@author: Gavi
"""

import numpy as np

# Create a 1D array of numbers from 1 to 10
array3 = np.arange(1,10)

# Extract all odd numbers from array of 1 10
# If a number divided by 2 has a remainder than it is an even number
a = array3[array3 % 2 == 1]
print('1D array of numbers from 1 to 10:',array3)
print('Odd numbers from array of 1 10:',a)


