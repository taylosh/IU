# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:55:18 2024

@author: stayl

DCSI-D590
Assignment 4
Shane_a04_q1.py
A program that takes an input string from the user and prints the string in a 
reverse order.
"""

def main():
    print("The program prints a string in a reverse order.")
    # Take the user input
    input_string = input("Please enter a string: ")
    # Get the length of the string
    string_length = len(input_string)
    # Loop through the string in reverse order using the final index
    for i in range(string_length - 1, -1, -1):
        # Print each character (without /n)
        print(input_string[i], end="")
    
main()
