# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:30:36 2024

@author: stayl

DCSI-D590
Assignment 7
Shane_a07_q1.py

Use a sentinel loop to write a program that prompts the user to enter a sequence 
of numbers (each number in a separate line) and prints:
• Total count of entered numbers
• The smallest of entered numbers
• The largest of entered numbers
• The count of positive numbers
• The count of negative numbers
The loop terminates when user enters an empty string (just hits Enter).
The program uses exception to catch if the user enters a non-number, then prints 
an error message and continues execution.
"""

def main():
    print('Program prints min, max, and count of positive and negative numbers.')
    count = 0
    smallest = None
    largest = None
    positive_count = 0
    negative_count = 0
    
    print("Enter numbers one by one. Press Enter again to stop.")
    
    while True:
        s = input("Enter a number: ")
        
        if s == "":
            break
        
        try:
            num = float(s)  # Allowing for float input
            count += 1
            
            # write in the first number and overwrite if next is smallest
            if smallest is None or num < smallest:
                smallest = num
            # write in the first number and overwrite if next is largest
            if largest is None or num > largest: 
                largest = num
            
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1

        except ValueError:
            print("Error! Please enter a valid number:")
    
    print(f"You entered {count} numbers.")
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
    print(f"There are {positive_count} positive and {negative_count} negative number(s).")

if __name__ == "__main__":
    main()
