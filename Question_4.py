# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:30:14 2024

@author: stayl

DCSI-D590
Assignment 2
question_4.py
An interactive Python calculator program.
"""

def main():
    # Print greeting
    print("Welcome to the Interactive Python Calculator\n")
    # Set the number of calculations the user can perform
    max_calcs = 100
    
    for _ in range(max_calcs):
        # Take the user input as an expression
        exp = input("Enter an expression: ")
        # Calculate the expression
        calc = eval(exp)
        print(calc)
    
main()
