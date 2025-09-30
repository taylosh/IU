# -*- coding: utf-8 -*-
"""
Created on Tue Jun 4 11:02:13 2024

@author: stayl

DCSI-D590
Assignment 5
Shane_a05_q2.py
A program which prints letter X in n lines using character c. 
n is a positive and odd integer. Write main() that prompts the user for n and 
c, and calls print_X(n, c) to print X in n lines using characters c.
"""

# Function that prints x
def print_X(n, c):
    for i in range(n):
        line = ""
        # Two loops that mirror each other to place the character
        for j in range(n):
            if j == i or j == (n - 1 - i):
                line += c
            else:
                line += " "
        print(line)

def main():
    n = int(input("Enter a positive and odd integer for the number of lines (n): "))
    if n % 2 == 0 or n <= 0:
        print("The number must be positive and odd.")
    else: 
        c = input("Enter the character to print the X: ")
        print_X(n, c)

main()
