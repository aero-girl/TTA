# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 5: Convert a 1D array to a 2D array with 2 rows
@author: Gavi
"""

import numpy as np

# Convert a 1D array to a 2D array with 2 rows
array5 = np.arange(0,20)

# Reshape to a 2D array with 2 rows 
# Setting to -1 automatically decides the number of cols
arr_shaped = array5.reshape(2, -1)  
print(arr_shaped)
print('1D array :',array5)
print('Reshaped to a 2D array with 2 rows:',arr_shaped)



