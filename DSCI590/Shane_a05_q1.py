# -*- coding: utf-8 -*-
"""
Created on Tue Jun 4 11:02:13 2024

@author: stayl

DCSI-D590
Assignment 5
Shane_a05_q1.py
A program that contains definitions for two functions:
• sum_n(n) returns the sum of the first n positive integers.
• sum_cubes(n) returns the sum of the cubes of the first n positive integers.
and a main()  function that prompts the user for a positive integer n, calls 
the above functions and prints out the sum of the first n integers and the sum 
of the cubes of the first n integers.at reads a file, counts and prints the 
number of words in the file.
"""

def sum_n(n):
    nums = [] 
    for i in range(0, n):
        nums.append(i+1)
    sums = 0
    for i in nums:
        sums = sums + i
    return sums


def sum_cubes(n):
    nums = []
    for i in range(0, n):
        nums.append(i+1)
    cubes = 0 
    for i in nums:
        cubes = cubes + (i**3)
    return cubes
    
def main():
    print("The program calculates the sum of first n numbers and sum of their cubes.")

    # Take the user input
    n = int(input("Please enter a positive integer: "))
    
    if n <= 0:
        print("You entered a number, which is not a positive integer.")
        return
    
    else:
        print("The sum of first", n, "positive integers is", sum_n(n))
        print("The sum of cubes of first", n, "positive integers is", sum_cubes(n))
    
main()
