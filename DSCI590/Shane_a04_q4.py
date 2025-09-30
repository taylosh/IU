# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:55:18 2024

@author: stayl

DCSI-D590
Assignment 4
Shane_a04_q4.py
A program that prompts the user for a string, determines if the string is a 
palindrome and prints "The string is palindrome" or "The string is not a palindrome."
"""

def main():
    print("The program checks if an input string is a palindrome.")
    # Take the user input
    input_string = input("Enter a string: ")
    # Initialize an empty string to store the reversed version of the input string
    reverse_string = ""
    # Get the length of the string
    string_length = len(input_string)
    # Loop through the string in reverse order using the final index
    for i in range(string_length - 1, -1, -1):
        # Append each character to the reverse string
        reverse_string += input_string[i]
    print("The reverse of this string is:", reverse_string)
    
    # Check if string is a palindrome - the string (should == reverse)
    if input_string == reverse_string:
        print("The string IS a palindrome.")
    else: 
        print("The string is NOT a palindrome.")
main()
