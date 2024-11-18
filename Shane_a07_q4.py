# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:30:36 2024

@author: stayl

DCSI-D590
Assignment 7
Shane_a07_q4.py

Write function is_prime(n) which takes a positive integer n as an input parameter 
and returns True if n is a prime number and False otherwise.
Write function print_prime(lower_limit, upper_limit) which prints all prime numbers 
between lower_limit and upper_limit (inclusive).
Function main() prompts user for positive integers lower_limit and upper_limit and
calls function print_prime to print prime numbers in the interval. main() prints 
error messages in case the entered numbers are not positive integers or if 
upper_limit < lower_limit.
"""

def is_prime(n):
    # Checks if a given number n is a prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def print_prime(lower_limit, upper_limit):

    print("The sequence of prime numbers in the given interval:")
    for num in range(lower_limit, upper_limit + 1):
        if is_prime(num):
            print(num)

def main():
    print("The program prints prime numbers in a range.")
    try:
        lower_limit = int(input("Enter the lower limit of a range: "))
        if lower_limit <= 1:
            print("Invalid input: Lower limit should be a positive integer, greater than 1.")
            return

        upper_limit = int(input("Enter the upper limit of the range: "))
        if upper_limit <= 1:
            print("Invalid input: Upper limit should be a positive integer, greater than lower limit.")
            return
        
        if upper_limit < lower_limit:
            print("Invalid input: Upper limit is less than lower limit.")
            return
        
        print_prime(lower_limit, upper_limit)
        
    except ValueError:
        print("Error! You entered a non-integer!")

if __name__ == "__main__":
    main()
