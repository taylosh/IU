# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:30:36 2024

@author: stayl

DCSI-D590
Assignment 7
Shane_a07_q2.py

Write the following functions:
• “to_numbers(nums)” that modifies each element of the list of strings nums by 
converting it to a number. Uses exception to catch a non-number and print “Error! 
The input is not a number”.
• “is_ascend(nums)” that returns True if the numbers in the list nums are in 
ascending order and False otherwise.
• “is_descend(nums)” that returns True if the numbers in the list nums are in 
descending order and False otherwise.
• “are_same(nums)” that returns True if the numbers in the list nums are the 
same, and False otherwise.
Write function main() that prompts the user for a sequence of numbers in a single 
line, separated by spaces, calls the above functions to determine if the numbers 
are ordered or same and accordingly prints “The numbers are in ascending order”, 
“The numbers are the same”, “The numbers are in descending order” or “The numbers 
are not sorted”. The function should check for special cases and print:
• “Error! No input number.”
• “You entered a single number.”
"""

def to_numbers(nums):
    # Start with a list of the itemss and verify they are numbers
    for i in range(len(nums)):
        try:
            nums[i] = float(nums[i])
        except ValueError:
            print("Error! The input is not a number!")
            return False
    return True

def is_ascend(nums):

    flag = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            flag = False
            break
    return flag

def is_descend(nums):

    flag = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            flag = False
            break
    return flag

def are_same(nums):
    match = nums[0]
    for num in nums:
        if num != match:
            return False
    return True

def main():
    print("A program to check if the input numbers are sorted.")
    # Take input nd break items by spaces
    input_str = input("Enter numbers separated by a space: ").strip()
    
    if not input_str:
        print("Error! No input number.")
        return
    
    nums = input_str.split()
    
    if len(nums) == 1:
        print("You entered a single number.")
        return
    
    if not to_numbers(nums):
        return
    
    if are_same(nums):
        print("The numbers are the same.")
    elif is_ascend(nums):
        print("The numbers are in ascending order.")
    elif is_descend(nums):
        print("The numbers are in descending order.")
    else:
        print("The numbers are not sorted.")

if __name__ == "__main__":
    main()
