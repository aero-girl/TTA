#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:07:41 2020
Write a program to ask a student for their percentage
mark, and convert this to a grade
@author: gavita
"""

def mark_grade(mark):
    if mark >= 90:
        #You achieved an A*
        grade = ("A*")
    elif mark >=80 and mark<90:
        #You achieved an A
        grade = ("A")
    elif mark >=70 and mark<80:
        #You achieved an B
        grade = ("B")
    elif mark >=60 and mark<70:
        #You achieved an C
        grade = ("C")
    else:
        #You achieved an F
        grade = ("F")

    return(grade)        
    
# Get student's mark
mark=input("Enter the student's mark: ")
grade = mark_grade(int(mark))
print ("Your grade is " + grade)
    