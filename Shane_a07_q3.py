# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:30:36 2024

@author: stayl

DCSI-D590
Assignment 7
Shane_a07_q3.py

Write the following functions:
• in_matrix() that prompts the user for the dimensions m and n of a matrix and 
gets the integers from the user (each integer in a separate line), which are the 
elements of the matrix. The function builds and returns a nested list mx with m 
elements, each element is a list of n integers. List mx represents an (m x n) 
matrix with integer elements. Let the program crash if the user inputs a non-integer.
• print_matrix (mx) that prints elements of matrix mx row by row.
• sum_rows(mx), which returns a list with elements that are the sums of numbers 
in mx rows.
Function main():
• Calls function in_matrix to get a matrix mx from the user,
• Calls function print_matrix(mx) to print the input matrix mx,
• Calls function sum_rows(mx) to sum the rows
"""

def in_matrix():
    # Prompts for dimensions m and n of a matrix and gets integers
    
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    
    mx = []
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Enter next element of row {i}: "))
            row.append(element)
        mx.append(row)
    
    return mx

def print_matrix(mx):
    # Prints elements of matrix mx row by row.
    for row in mx:
        print("\t".join(map(str, row)))

def sum_rows(mx):
    sums = []
    for i, row in enumerate(mx):
        row_sum = 0
        for element in row:
            row_sum += element
        sums.append(row_sum)
        print(f"Sum of numbers in row {i} is {row_sum}")
    return sums

def main():
    print("Program to sum the rows of an input matrix.")
    mx = in_matrix()
    print("\nThe input matrix is:")
    print_matrix(mx)
    


if __name__ == "__main__":
    main()
