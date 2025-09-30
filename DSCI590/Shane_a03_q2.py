# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q2.py
A program to determine the length of a ladder (in feet) required to reach a 
given height when leaned against a house.
"""

import math 

# Define the function
def ladder():
    print("This program calculates the length of a ladder.\n")
    # Take the user input as a number (float)
    ht, deg = eval(input("Please enter the height in feet and the angle in degrees (h,d): "))
    # convert degrees to radians
    rad = (math.pi /180) * deg
    # calculates required length of ladder
    ln = ht / math.sin(rad)
    round_ln = round(ln, 2)
    print("The length of the ladder is", round_ln,"feet.")

# Initalize the program
ladder()
