# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:30:14 2024

@author: stayl

DCSI-D590
Assignment 2
question_3.py
A program to compute and print a table of Celsius temperatures and the 
Fahrenheit equivalents every 10 degrees from 0 C to 100 C
"""

def main():
    # Print table header
    print("Conversion table from Celsius to Fahrenheit\n\n","Celsius\tFarenheit\n",
          "--------------------")
    for i in range(11):
        celsius = (i)*10
        fahrenheit = (9/5) * celsius + 32
        print(celsius, "\t"*3, fahrenheit)

main()