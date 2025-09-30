# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q4.py
A program to sum a series of numbers entered by the user
"""

def calc_sum():
    print("The program calculates the sum of numbers entered by the user.")
    # Prompt the user for input of total numbers (float)
    t = eval(input("How many numbers do you want to sum up? "))
    # initialize sum
    s = 0
    for i in range(t):
        # Take the user input as an number (float)
        n = eval(input("Enter a number: "))
        # Add the number to sum
        s = s + n
        
    print("The sum of the", t, "numbers is:", s)

calc_sum()