# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:37:05 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_a10_q2.py

Write function “rel_std(stock_data)” which receives the stock data downloaded 
from a web site, and returns a relative standard deviation (which is standard 
deviation of the stock close values divided by the stock close value average 
and multiplied by 100). Function “main()”:
• Downloads stock data for year 2022 for 8 Dow Jones companies:
Boeing, Coca-Cola, Exxon Mobil, General Electric, JPMorgan Chase, Nike, Pfizer, Verizon
• Calls “rel_std(stock_data)” to collect relative standard deviation for the companies.
• Stores relative standard deviations in a dictionary, with company stock symbol 
as a key and relative standard deviation as value.
• Print the company names and corresponding relative standard deviations. It is 
not important if the order of the companies is not the same as when you inserted 
them into the dictionary.
Print all numbers rounded to two decimal places.
"""

import pandas as pd
import yfinance as yf

# calclate relative standard deviation
def rel_std(stock_data):
    close_values = stock_data['Close']
    n = len(close_values)
    average_close = close_values.mean()
    variance_close = ((close_values - average_close) ** 2).sum() / (n - 1)
    std_dev_close = variance_close ** 0.5
    rel_std = (std_dev_close / average_close) * 100
    return rel_std

# download stock data 
def download_stock_data(symbol, year):
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Main function 
def main():
    # Dictionary for company names and symbols
    companies = {
        'Boeing': 'BA',
        'Coca-Cola': 'KO',
        'Exxon Mobil': 'XOM',
        'General Electric': 'GE',
        'JPMorgan Chase': 'JPM',
        'Nike': 'NKE',
        'Pfizer': 'PFE',
        'Verizon': 'VZ'
    }
    
    # Dictionary for relative standard deviations
    rel_std_dict = {}
    
    # Iterate over company
    for company, symbol in companies.items():
        # Download for year 2022
        stock_data = download_stock_data(symbol, 2022)
        
        # Calculate relative standard deviation
        relative_std = rel_std(stock_data)
        
        # Store
        rel_std_dict[company] = round(relative_std, 2)
    
    # Print esults
    print("Program that calculates relative standard deviation for eight Dow Jones companies.")
    print("Company\t\tRelative std deviation")
    print("---------------------------------------------")
    for company, std_dev in rel_std_dict.items():
        print(f"{company}\t\t{std_dev}")

# Execute the main function
if __name__ == "__main__":
    main()
