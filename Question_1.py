# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:30:14 2024

@author: stayl

DCSI-D590
Assignment 2
question_1.py
A program to convert kilometers to miles
"""
# Define the function
def main():
    print("This program converts kilometers to miles.")
    # Take the user input as a number (float)
    km = eval(input("Enter the distance in kilometers:"))
    # Convert to miles
    miles = km*0.62
    print("The distance is", miles,"miles.")

# Initalize the program
main()
