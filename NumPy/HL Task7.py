# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:12:20 2020
Home Learning Task 7: Create the following pattern without hardcoding. Use only NumPy
functions and the below input array
@author: Gavi
"""

import numpy as np

# Create array
a = np.array([1,2,3])

# Repeat elements of an array
a1 = np.repeat(a, 3)

# Construct an array by repeating A the number of times given by reps.
a2 = np.tile(a, 3)

# Stack arrays in sequence horizontally (column wise).
array7 = np.hstack((a1,a2))
print('Aray created from repeat and tile: ', array7)
