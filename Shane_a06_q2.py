# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:12 2024

@author: stayl

DCSI-D590
Assignment 6
Shane_a06_q2.py

Write a function body_mass_index(height, weight) which receives height in 
inches and weight in pounds, converts height to meters and weight to kilograms,
then calculates and returns the BMI.
Function main() prompts for person’s height in inches and weight in pounds, 
calls body_mass_index(height, weight) to determine BMI and prints the BMI and 
a message telling whether the person is above, within or below the healthy range.
Function main() uses exception to check if the user enters a non-number. 
The function prints an error message and quits if the user enters a non-number 
or a negative number.
"""

def body_mass_index(height, weight):
    
    # Convert height to meters (1 inch = 0.0254 meters)
    height_meters = height * 0.0254
    
    # Convert weight to kilograms (1 pound = 0.453592 kilograms)
    weight_kilograms = weight * 0.453592
    
    # Calculate BMI
    bmi = weight_kilograms / (height_meters ** 2)
    
    return bmi


def main():
    print('This program calculates the body mass index.')
    try:
        # Prompt the user for height in inches
        height_input = input("Enter your height in inches:")
        height = float(height_input)

    except ValueError:
        # Handle the case where the input is not a number
        print("Error! You entered a non-number.")
        return

    try:
        # Prompt the user for weight in pounds
        weight_input = input("Enter your weight in pounds:")
        weight = float(weight_input)   
        
    except ValueError:
        # Handle the case where the input is not a number
        print("Error! You entered a non-number.")
        return
     
        # Check if the height and weight are positive numbers
    if height <= 0 or weight <= 0:
        print("Error! You entered a negative number!")
        return
        
    # Calculate BMI
    bmi = body_mass_index(height, weight)
    if bmi > 25:
        comment = 'above'
    elif 19 < bmi < 25:
        comment = 'within'
    elif bmi < 19:
        comment = 'under'
            
    # Print the BMI
    print(f"Your BMI is {bmi}, you are {comment} the healthy range!")
    
# Run the main function
if __name__ == "__main__":
    main()
