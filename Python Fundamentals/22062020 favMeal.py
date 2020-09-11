#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:55:01 2020
Write a program that allows user to enter his favourite starter, main
course, dessert and drink. Output a message which says – “Your
favourite meal is ………with a glass of….”
@author: gavita
"""

starter = input("Enter your favourite starter: ")
main = input("Enter your favourite main course: ")
dessert = input("Enter your favourite dessert: ")
drink = input("Enter your favourite drink: ")


print ("Your favourite meal is " + starter + " and " + main + " with a glass of " \
       + drink + " and " + dessert + " for dessert!")
