# -*- coding: utf-8 -*-
"""
Created on Tue Jun 4 11:02:13 2024

@author: stayl

DCSI-D590
Assignment 5
Shane_a05_q3.py
A program that calculates the factorial of a positive integer m. Write main() 
function which uses function factorial to calculate the number of combinations 
of n objects, taken r objects at a time. Math symbol for factorial of m is “m!”.
The formula to calculate the number of combinations (C):
C(n, r) = n!/(r! ∙ (n-r)!)
"""

import math 

def main():
    print("Calculates the number of combinations of n objects taken r at a time.")
    
    n = int(input("Enter a positive integer n: "))
    if n < 0:
        print("n must be a positive integer.")
    else:
        r = int(input("Enter a positive integer r: "))
        if n <= r:
            print("Error! Number n is less than r!")
        else:
            m = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
            print(f"The number of combinations C({n}, {r}) is: {m}")

# Call the main function to execute the program
main()
