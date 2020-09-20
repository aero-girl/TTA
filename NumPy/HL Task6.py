# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 6: Create two arrays a and b, stack these two arrays 
vertically use the np.dot and np.sum to calculate totals
@author: Gavi
"""

import numpy as np

# Create two arrays a and b
a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print('Array 1: \n',a)
print('Array 2: \n',b)

# Stack these two arrays vertically use the np.dot
# Matrix multiplication of 2 matrice of the same size
c = np.dot(a,b)
print('Stacked array: \n',c)


# Use np.sum to calculate totals
sum = np.sum (c)
print('Total sum is: \n', sum)


