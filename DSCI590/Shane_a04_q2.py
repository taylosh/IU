# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:55:18 2024

@author: stayl

DCSI-D590
Assignment 4
Shane_a04_q2.py
A program that takes a positive integer number from the user and prints the 
number in words.
"""

def main():
    print("The program spells the input number.")
    # Take the user input
    input_number = input("Please input a number: ")
    # Display typed number
    print("You typed number: ", input_number)
    # Lists to map digits to words
    nums = "0123456789"
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             'eight', 'nine']
    
    # Print the number in words
    print("The number in words:", end=" ")

    # Loop through input_number and print the corresponding word
    for n in input_number:
        # Find the index of the digit in nums
        i = nums.index(n)
        # Print the corresponding word with space
        print(words[i], end=" ")
    
main()
