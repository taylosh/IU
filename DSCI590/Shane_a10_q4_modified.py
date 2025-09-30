# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:04:38 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_a10_q4.py

Write function “max_up(stock)” that receives a DataFrame “stock” with stock data 
and finds out the maximum period in which the close value of the stock was up 
each day. Consider the stock up if the close value is greater than the close value 
of the previous day.
Function returns the number of (working) days in the period and index of the 
period start.
Function “main()”:
• Prompts the user for the stock symbol and downloads the stock data for the year 
2022 into a DataFrame “df”.
• Calls function “max_up(df)” to get the number of days of the max period the 
stock was up each day, and the index of the period start.
• Prints the period length in days, date of period start and period end. (“days” 
refer to the days the stock exchange was open - the days listed in the DataFrame “df”.)
"""

import pandas as pd
import yfinance as yf # GABE

def max_up(stock):
    max_length = 0
    max_start_index = 0
    current_length = 1
    current_start_index = 0
    
    for i in range(1, len(stock)):
        if stock["Close"][i] > stock["Close"][i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = current_start_index
            current_length = 1
            current_start_index = i
    
    # Check at the end 
    if current_length > max_length:
        max_length = current_length
        max_start_index = current_start_index
    
    return max_length, max_start_index

def main():
    # Prompt for stock 
    stock_symbol = input("Please enter the stock symbol: ").upper()
    
    # Download stock data for 2022
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    
    # was still having issues so I included this 
#    try:
#        import pandas_datareader.data as web
#    except ImportError:
#        print("Problem with pandas_datareader")
#        return
    
    try:
#        df = web.DataReader(stock_symbol, 'yahoo', start_date, end_date)
        df = yf.download(stock_symbol, start=start_date, end=end_date, progress=False) # GABE
    except:
        print(f"Error: Empty data for stock symbol {stock_symbol}")
        return
    
    # Call max_up function 
    max_days, start_index = max_up(df)
    
    # Determine the start and end 
    period_start_date = df.index[start_index].strftime('%Y-%m-%d')
    period_end_date = df.index[start_index + max_days - 1].strftime('%Y-%m-%d')
    
    # Print 
    print(f"The longest up period for the stock symbol {stock_symbol}:")
    print(f"Length in days: {max_days}")
    print(f"Period started on: {period_start_date}")
    print(f"Close stock value at start: {df['Close'][period_start_date]:.2f}")
    print(f"Period ended on: {period_end_date}")
    print(f"Close stock value at end: {df['Close'][period_end_date]:.2f}")

# Running the main function
if __name__ == "__main__":
    main()