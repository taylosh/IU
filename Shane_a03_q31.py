# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q31.py
A program that asks the user for a positive integer n and then prints all numbers 
between 1 and n, inclusive, which are divisible by 3
"""

def mult_of_3():
    print("This program prints the numbers divisible by 3.")
    # Take the user input as a number (int)
    n = int(input("Please enter a positive integer: "))
    # initialize list
    nums = []
    # iterate ofer range from 1 to input    
    for i in range(1, n+1):
        if (i % 3) == 0:
            nums.append(i)
    if len(nums) == 1: 
        print("The number that is divisible by 3 between 1 and", n, "is:", nums)
    else:
        print("The numbers that are divisible by 3 between 1 and", n, "are:", nums)
mult_of_3()
