# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 8: In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) 
remove all repeating items present in array b
@author: Gavi
"""

import numpy as np

# Create arrays
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])

# Remove all repeating items present in array b
# setdiff1d: Find the set difference of two arrays.
array_diff = np.setdiff1d(b,a)

print('Array 1: ',a)
print('Array 2: ',b)
print('Removed all repeating items present in array 2 :', array_diff)