# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:05:14 2024

@author: stayl

DCSI-D590
Assignment 3
Shane_a03_q1.py
A program that calculates and prints the wind chill
"""

import math 

# Define the function
def wind_chill():
    print("This program calculates the wind chill.")
    # Take the user input as a number (float)
    far, winsp = eval(input("Enter the temperature in degrees Fahrenheit wind speed in miles per hour(T,V): "))
    # calculate and print wind chill rounded to one digit
    chill = 35.74 + (0.6215 * far) - (35.75*(math.pow(winsp, 0.16))) + (0.4275*far*(math.pow(winsp, 0.16)))
    round_chill = round(chill, 1)
    print("The wind chill index is", round_chill)

# Initalize the program
wind_chill()
