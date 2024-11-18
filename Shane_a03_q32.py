# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q32.py
A program that asks the user for a positive integer n and then uses the counter
pattern to find out and print the count of all numbers between 1 and n, 
inclusive, which are divisible by 7.
"""

def count_div_7():
    print("This program prints the count of numbers divisible by 7.")
    # Take the user input as a number (int)
    n = int(input("Please enter a positive integer: "))
    # initialize count
    c = 0
    # iterate ofer range from 1 to input    
    for i in range(1, n+1):
        if (i % 7) == 0:
            c += 1
    # print result
    if c == 1:
        print("There is", c, "number between 1 and", n, "that is divisible by 7.")
    else:
        print("There are", c, "numbers between 1 and", n, "that are divisible by 7.")
count_div_7()