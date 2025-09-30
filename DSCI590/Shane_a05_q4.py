# -*- coding: utf-8 -*-
"""
Created on Tue Jun 4 11:02:13 2024

@author: stayl

DCSI-D590
Assignment 5
Shane_a05_q4.py
Write the following functions:
• square_each(nums), nums is a list of numbers. 
    Modifies the list nums by squaring each entry. 
• sum_list(nums), nums is a list of numbers. 
    Returns the sum of the numbers in the list. 
• to_numbers(str_list), str_list is a list of strings, where each string 
    represents a number. 
    Modifies each string in the list by converting it to a number. 
Write a main() that uses the previous three functions to compute the 
sum of the squares of numbers in each line in a file. 
The file contains several lines; each line contains numbers separated by spaces. 
The main() should prompt for a file name and print out the sum of the squares 
of the numbers in each line in the file.
"""

def square_each(nums):
    # Square each number in the list nums
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sum_list(nums):
    # Returns the sum of the numbers in the list nums
    return sum(nums)

def to_numbers(str_list):
    # Converts a list of strings to a list of numbers
    for i in range(len(str_list)):
        str_list[i] = eval(str_list[i])

def main():
    print("The program prints the sum of squares of each line in a file.")
    # Ask for file name
    file_name = input("Enter the file name: ")
    # Open the file
    file= open(file_name, 'r')
    for line in file:
        # Break up the line (string) into a list of the words
        words = line.split()
        # Compute the sum of the squares of numbers in each line of the file
        to_numbers(words)
        square_each(words)
        total = sum_list(words)
        print(f"Sum of squares: {total}")

main()
