# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:47:05 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_a10_q4.py

Write function “max_up(stock)” that receives a DataFrame “stock” with stock data 
and finds out the maximum period in which the close value of the stock was up each 
day. Consider the stock up if the close value is greater than the close value of 
the previous day.
Function returns the number of (working) days in the period and index of the period 
start.

Function “main()”:
• Prompts the user for the stock symbol and downloads the stock data for the 
year 2022 into a DataFrame “df”.
• Calls function “max_up(df)” to get the number of days of the max period the 
stock was up each day, and the index of the period start.
• Prints the period length in days, date of period start and period end. (“days” 
refer to the days the stock exchange was open - the days listed in the DataFrame “df”.)
"""

def max_up(stock):
    max_up_length = 0
    max_up_start_date = None
    max_up_end_date = None
    current_up_length = 0
    current_up_start_date = None
    
    for i in range(1, len(stock)):
        if stock["Close"][i] > stock["Close"][i-1]:
            if current_up_length == 0:
                current_up_start_date = stock.index[i-1].date()
            current_up_length += 1
        else:
            if current_up_length > max_up_length:
                max_up_length = current_up_length
                max_up_start_date = current_up_start_date
                max_up_end_date = stock.index[i-1].date()
            current_up_length = 0
            current_up_start_date = None
    
    # Check at the end of the loop
    if current_up_length > max_up_length:
        max_up_length = current_up_length
        max_up_start_date = current_up_start_date
        max_up_end_date = stock.index[len(stock)-1].date()
    
    return max_up_length, max_up_start_date, max_up_end_date

def main():
    import pandas_datareader.data as web
    from datetime import datetime
    
    # Prompt user for stock symbol
    stock_symbol = input("Please enter the stock symbol: ").upper()
    
    # Define date range for 2022
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2022, 12, 31)
    
    # Download stock data into a DataFrame 'df'
    df = web.DataReader(stock_symbol, 'yahoo', start_date, end_date)
    
    # Call max_up function to get the maximum up period information
    max_up_length, max_up_start_date, max_up_end_date = max_up(df)
    
    # Retrieve close prices at start and end of the period
    if max_up_start_date is not None and max_up_end_date is not None:
        start_close_price = df.loc[max_up_start_date]['Close']
        end_close_price = df.loc[max_up_end_date]['Close']
        
        # Print the results
        print(f"The longest up period for the stock symbol {stock_symbol}:")
        print(f"Length in days: {max_up_length}")
        print(f"Period started on: {max_up_start_date}")
        print(f"Close stock value at start: {start_close_price:.2f}")
        print(f"Period ended on: {max_up_end_date}")
        print(f"Close stock value at end: {end_close_price:.2f}")


main()
