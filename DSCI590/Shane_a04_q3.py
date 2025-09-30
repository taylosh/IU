# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:55:18 2024

@author: stayl

DCSI-D590
Assignment 4
Shane_a04_q3.py
A program  that calculates the numeric value of a single name (in lower case 
letters) provided as input.
"""
# Define function that assigns value to each letter and sums them
def nam_val(name):
    value = 0
    for letter in name:
        # Calculate distance from 'a' to get letter value; take away 'a' because 
        # the Unicode values for lower case don't start with 1 (it's 90-something);
        # because that would make a = 0, add 1 back
        value += ord(letter) - ord('a') + 1
    return value
    
def main():
    print("The program computes the value of a string.")
    # Take the user input
    name = input("Enter any name in lower case: ")
  
    num_val = nam_val(name)
    print("The numeric value of the name is: ", num_val)
    
main()
