# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:37:05 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_a10_q1.py

Use pandas to download IBM stock data for year 2022 into a DataFrame, calculate 
and print the variance of close values using the given formula.
-xi is the stock close value on day i, x̅ is the mean (average) of all stock close 
values in 2022 and n is
the number of rows in the DataFrame (equal to number of days the stock exchange 
was open in 2022). Calculate and print the standard deviation.
Find and print max and min closing stock values and the respective dates.
Print all numbers rounded to two decimal places.   
"""
import pandas as pd
import yfinance as yf

# Download IBM stock data for 2022
df = yf.download("IBM", start="2022-01-01", end="2022-12-31")

# Calculate statistics
close_values = df["Close"]
n = len(close_values)
average_close = close_values.mean()
variance_close = ((close_values - average_close) ** 2).sum() / (n - 1)
std_dev_close = variance_close ** 0.5
max_close = close_values.max()
max_date = df.loc[df["Close"].idxmax()].name.date()
min_close = close_values.min()
min_date = df.loc[df["Close"].idxmin()].name.date()

# Print rounded to two decimals
print("\nProgram that calculates IBM stock data statistics for year 2022.")
print(f"There are {n} rows of stock data.")
print(f"IBM 2022 average stock value: {average_close:.2f}")
print(f"IBM stock variance: {variance_close:.2f}")
print(f"IBM stock standard deviation: {std_dev_close:.2f}")
print(f"The max stock value {max_close:.2f} was on {max_date}")
print(f"The min stock value {min_close:.2f} was on {min_date}")
