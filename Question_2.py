# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:30:14 2024

@author: stayl

DCSI-D590
Assignment 2
question_2.py
A program to convert mileage to liters per 100 km
"""
# Define the function
def main():
    print("The program converts mileage to liters per 100 km.\n")
    # Take the user input as a number (float)
    mpg = eval(input("Please enter mileage (miles per gallon):"))
    print("\nVehicle economy is", mpg,"miles per gallon.")
    # Calculate consumption in liters per 100 km
    # Conversions: kilometers per mile, liters per gallon
    kpm = 1.6
    lpg = 3.785
    # Convert miles per gallon to kilometers per liter
    kpl = (mpg * kpm) / lpg
    # Convert kilometers per liter to liter per 100 kilometers
    lp100k = 100 / kpl
    print("Vehicle consumption is", lp100k,"liters per 100 km.")

# Initalize the program
main()
