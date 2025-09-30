# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:12 2024

@author: stayl

DCSI-D590
Assignment 6
Shane_a06_q1.py

Write a function letter_grade(score), which receives a score and uses decision 
structure to calculate and return the corresponding letter grade.
Function main() prompts the user for the score. Use exception to check if the 
user enters a string that does not represent a number. If the user enters a 
non-number or a number outside range 0 to 100, main() prints appropriate message 
and terminates.
Function main() calls letter_grade to convert the score into a letter grade and 
prints the letter grade.
"""

def letter_grade(score):
    # convert a numerical score into a letter grad
    if 93 <= score <= 100:
        return 'A'
    elif 90 <= score < 92.99:
        return 'A-'
    elif 86 <= score < 89.99:
        return 'B+'
    elif 83 <= score < 85.99:
        return 'B'
    elif 80 <= score < 82.99:
        return 'B-'
    elif 76 <= score < 79.99:
        return 'C+'
    elif 73 <= score < 75.99:
        return 'C'
    elif 70 <= score < 72.99:
        return 'C-'
    elif 66 <= score < 69.99:
        return 'D+'
    elif 60 <= score < 65.99:
        return 'D'
    else:
        return 'F'


def main():
    # prompt the user for a score and check for exceptions
    #then print the corresponding letter grade.
    print('This program calculates the letter grade from a total score.')
    try:
        in_string = input("Enter your total score (0-100): ")
        
    except ValueError:
        # Handle the case where the input is not a number
        print("Error! You entered a string that is not a number!")

    # Convert input to a float
    score = float(in_string)
        
    # Check if the score is within the valid range
    if score < 0 or score > 100:
        print("Error! The total score must be between 0 and 100.")
        return
        
    # Print the letter grade
    else:
        # Get the letter grade
        grade = letter_grade(score)
        print(f"The letter grade for a score of {score} is {grade}.")
    
# Run the main function
if __name__ == "__main__":
    main()
