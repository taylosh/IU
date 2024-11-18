# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q5.py
A program, which prompts the user for two positive start and end integers, that
define a range of numbers, including both start and end and then calculates and
prints the ratio of the sum of even numbers to the sum of all the numbers in the
range (rounded to three decimal digits).
"""

def rat_sum():
    # take the user input as starting number (int)
    s = int(input("Enter a positive start number of the range: "))
    # take the user input as ending number (int)
    e = int(input("Enter a positive end number of the range: "))
    # calculate sum of ALL numbers in the range
    # initialize sum
    sum_all = 0
    for i in range(s, e+1):
        # Add the number to sum of all
        sum_all = sum_all + i

    # calculate sum of EVEN numbers in the range
    # initialize sum
    sum_even = 0
    for i in range(s, e+1):
        # check if i is even
        if (i % 2) == 0:
            # add the even number to sum of evens
            sum_even = sum_even + i

    rat = sum_even/sum_all
    print("The ratio of the sum of even numbers to the sum of all numbers in the range is:", round(rat, 3))

rat_sum()
