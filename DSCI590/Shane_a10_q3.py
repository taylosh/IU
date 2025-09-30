# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:47:05 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_a10_q3.py

Write function “correl(stock1, stock2)” which receives the stock data of two 
companies and returns sample correlation between their close values:
• cov(close1, close2) is the sample covariance between stock close values of stock1 
and stock2.
• std(close1) and std(close2) are sample standard deviations of the stock1 and 
stock2, respectively.

Function “main()”:
• Downloads Boeing and Coca-Cola stock data for 2022
• Calls “correl(stock1, stock2)” to get and print the sample correlation between 
the close values of the two companies.
Print the numbers rounded to two decimal places.
"""

import pandas as pd

def cov(close1, close2):
    n = len(close1)
    mean_close1 = close1.sum() / n
    mean_close2 = close2.sum() / n
    covariance = ((close1 - mean_close1) * (close2 - mean_close2)).sum() / (n - 1)
    return covariance

def std(close):
    n = len(close)
    mean_close = close.sum() / n
    variance = ((close - mean_close) ** 2).sum() / (n - 1)
    std_dev = variance ** 0.5
    return std_dev

def correl(stock1, stock2):
    close1 = stock1['Close']
    close2 = stock2['Close']
    
    covariance = cov(close1, close2)
    std_close1 = std(close1)
    std_close2 = std(close2)
    
    correlation = covariance / (std_close1 * std_close2)
    return correlation

def main():
    # Download stock data for 2022
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    ticker_symbols = ['BA', 'KO']
    
    # get data using pandas_datareader (had some issues with this so I check its installed)
    try:
        import pandas_datareader.data as web
    except ImportError:
        print("Problem with pandas_datareader")
        return
    
    # getting data
    stock_data = {}
    for ticker in ticker_symbols:
        stock_data[ticker] = web.DataReader(ticker, 'yahoo', start_date, end_date)
    
    # close prices
    boeing_data = stock_data['BA']
    coke_data = stock_data['KO']
    
    # Calculate  
    avg_boeing = boeing_data['Close'].sum() / len(boeing_data['Close'])
    std_boeing = std(boeing_data['Close'])
    avg_coke = coke_data['Close'].sum() / len(coke_data['Close'])
    std_coke = std(coke_data['Close'])
    
    covariance = cov(boeing_data['Close'], coke_data['Close'])
    correlation = correl(boeing_data, coke_data)
    
    # results
    print("Program calculates sample correlation between Boeing and Coca Cola closing stock values in 2022.")
    print(f"Average Boeing stock value: {avg_boeing:.2f}")
    print(f"Std deviation of Boeing stock: {std_boeing:.2f}")
    print(f"Average Coke stock value: {avg_coke:.2f}")
    print(f"Std deviation of Coke stock: {std_coke:.2f}")
    print(f"Covariance: {covariance:.2f}")
    print(f"Correlation between BA and KO: {correlation:.2f}")

if __name__ == "__main__":
    main()
