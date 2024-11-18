# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:12 2024

@author: stayl

DCSI-D590
Assignment 6
Shane_a06_q3.py

Write function in_date() that prompts the user for a month, day and year and 
returns a list [month, day, year]. Assume that the user enters a string for a 
month, and integers for day and year. Don’t perform validity check of the user 
inputs.
Write function is_month(month) that returns True if month is a valid month name 
and False otherwise.
Write function is_day(month, day) that returns True if the day is a valid day 
in month, and False otherwise.
Write function is_leap_year(year) that returns True if year is a leap year, and 
False otherwise.
Write function main() that uses function in_date() to get a date as a list [month, 
day, year] and calls the other three functions to determine if the [month, day, 
year] is a valid date in a leap year.
"""

def in_date():
    # Prompts the user for a month, day, and year
    month = input("Please enter the month: ")
    day = int(input("Enter the day: "))
    year = int(input("Enter the year: "))
    return [month, day, year]

def is_month(month):
    # Retrns True if month is a valid month name, False otherwise.
    valid_months = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]
    return month in valid_months

def is_leap_year(year):
    # Returns True if year is a leap year, False otherwise.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def is_day(month, day, year):
    # Returns True if the day is a valid day in month, False otherwise.
    m31 = ["January", "March", "May", "July", "August", "October", "December"]
    m30 = ["April", "June", "September", "November"]
    if month in m31:
        return 1 <= day <= 31
    elif month in m30:
        return 1 <= day <= 30
    elif month == "February":
        if is_leap_year(year):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28
    else: 
        return False

def main():
    print("The program determines a valid date in a leap year.")
    # Get a date and determine if it is valid and in a leap year.
    date = in_date()
    month, day, year = date
    
    if not is_month(month):
        print("Error! You entered an invalid month name.")
        return
    
    if not is_day(month, day, year):
        print(f"Error! You entered an invalid day in {month}.")
        return
    
    if is_leap_year(year):
        print("You entered a valid date in a leap year!")
    else:
        print("This is not a valid date in a leap year.")

# Run the main function
if __name__ == "__main__":
    main()

