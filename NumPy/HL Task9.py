# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 9: Get all items between 5 and 10 from a and b 
and sum them together
@author: Gavi
"""

import numpy as np

# Create arrays
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])

# Stack arrays in sequence horizontally (column wise).
c = np.hstack((a,b))

# Find values between 5 and 10
c_array = c[(c >= 5) & (c <= 10)]

# Sum them all together
sum = np.sum (c_array)
print('Array 1: ',a)
print('Array 2: ',b)
print('Stacked array in sequence horizontally :',c)
print('Extracted values between 5 and 10 from stacked array:',c_array)
print("The sum is:", sum)

