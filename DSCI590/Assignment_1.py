# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:22:48 2024

@author: stayl

DCSI-D590
Assignment 1
"""
# Q2 Instructions: On slide 7, lecture 1.6, there is an example of a function 
# with an input parameter (argument). Use this pattern to write function 
# definitions for the following tasks.

## 2.1 circle_area(r)

def circle_area(r):
    print(3.14*(r**2))

##Check sample
circle_area(2)

## 2.2 kilometers_to_miles(km)

def kilometers_to_miles(km):
    print(km*0.62)

##Check sample
kilometers_to_miles(600)
    
## 2.3 square_area(side)

def square_area(side):
    print(side**2)
    
##Check sample
square_area(12)
    
# Q3 Instructions: Use “for” loop and “range” function to write function 
# definitions for the following tasks.

## 3.1 first_five_squares()

def first_five_squares():
    for i in range(1, 6):
        print(i**2)

##Check sample
first_five_squares()

## 3.2 first_ten_reversed()

def first_ten_reversed(n):
    for i in range((-n), 0, 2):
        print(i*(-1))
        
##Check sample
first_ten_reversed(20)