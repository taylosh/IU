# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:12 2024

@author: stayl

DCSI-D590
Assignment 6
Shane_a06_q5.py

A website requires the users to input username and password to register. Write 
a program to check the validity of password input by users. Following are the 
criteria for checking the password:
• Minimum length of password: 4 characters
• Maximum length of password: 8 characters
• First character has to be a letter
• The password much contain at least one digit ( 0, 1, … , 9)
• The password must contain at least one character from ( $ # @)
In case a user enters an invalid password, the program prints an error message 
indicating the type of error and quits.
"""

def check_password(password):
    # Minimum length 4 characters
    if len(password) < 4:
        print("Error: The password has less than 4 characters!")
        return False
    
    # Maximum length of password: 8 characters
    if len(password) > 8:
        print("Error: The password has more than 8 characters!")
        return False
    
    # First character has to be a letter
    if not password[0].isalpha():
        print("Error: The first character of the password must be a letter.")
        return False
    
    # Password must contain at least one digit (0-9)
    contains_digit = False
    for char in password:
        if char.isdigit():
            contains_digit = True
            
    if contains_digit == False:
        print("Error: The password does not have at least one digit.")
        return False
    
    # Password must contain at least one character from [$ # @]
    special_char = False
    for char in password:
        if char in "$#@":
            special_char = True

    if special_char == False:
        print("Error: The password does not have at least one character from [$#@]!")
        return False
    
    return True

def main():
    password = input("Please enter a password: ")
    
    if check_password(password):
        print("You entered a valid password")


# Run the main function
if __name__ == "__main__":
    main()
   