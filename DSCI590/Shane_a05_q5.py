# -*- coding: utf-8 -*-
"""
Created on Tue Jun 4 11:02:13 2024

@author: stayl

DCSI-D590
Assignment 5
Shane_a05_q5.py
Write function count_digits(line), which counts and returns the number of digits 
in a string line. 
Write a main() that prompts the user for the name of a text file, and uses the 
previous function to count and print the total number of digits in each line 
of the text file.
"""

# Count function
def count_digits(line):
    count = 0
    for c in line:
        if c.isdigit():
            count += 1
    return count

def main():
    print("The program prints the number of digits in each line of a file.")
    # Prompt user for the name of a text file 
    file_name = input("Enter the file name: ")
    # Open the file
    file= open(file_name, 'r')
    # Read in lines
    lines = file.readlines()
    
    # Loop through lines with count function        
    for i, line in enumerate(lines, 1):  
        # Start counting from line 1
        digits = count_digits(line)
        # Print the total number of digits and line number
        print("There are", digits, "digits in line", i)

main()