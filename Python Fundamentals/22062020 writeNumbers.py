#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:44:34 2020
Write a program that allows you to enter 4 numbers and stores them in file called Numbers
@author: gavita
"""

# define variable to store numbers to write to file
numList = ["3", "45", "83",  "21"]

# open a file to write
myFile = open("Numbers.txt","w")

# Iterate through the list and write each number on a separate line
for element in numList:
     myFile.write(element)
     myFile.write('\n')
myFile.close()