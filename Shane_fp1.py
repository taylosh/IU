# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:12:45 2024

@author: stayl

DCSI-D590
Assignment 10
Shane_fp1.py

Phase 1 objectives: 
    Load dataset into Python
    Impute missing value to column A7 - using mean
    Find the mean, median, standard deviation and variance of each of the attributes
A2 to A10
    Plot histograms with 10 bins for attributes A2 to A10 (nine histograms)
    
"""

import pandas as pd
import matplotlib.pyplot as plt

## Retrieving data
def load_data():
    # Define columns
    col = ["Scn", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Class"]
    # Load data
    df = pd.read_csv('breast-cancer-wisconsin.data', na_values='?', names=col)
    return df

## Impute missing values
def impute_missing_values(df):
    # Compute A7 mean without NaNs
    a7_mean = df['A7'].mean(skipna=True)
    # Replace NaNs in A7 with mean
    df['A7'] = df['A7'].fillna(a7_mean)
    return df

## Running stats
# Functions for stats
def mean(column):
    return sum(column) / len(column)

def median(column):
    sorted_col = sorted(column)
    n = len(sorted_col)
    midpoint = n // 2
    if n % 2 == 1:
        return sorted_col[midpoint]
    else:
        return (sorted_col[midpoint - 1] + sorted_col[midpoint]) / 2

def variance(column):
    column_mean = mean(column)
    return sum((x - column_mean) ** 2 for x in column) / len(column)

def standard_deviation(column):
    return variance(column) ** 0.5

## Calculate stats and plot histograms
def calculate_stats_and_plot(df):
    # Define columns
    col = ["Scn", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Class"]
    
    for col_name in col[1:10]:
        column_data = df[col_name].astype(float).tolist()  # Convert to list of floats
        col_mean = round(mean(column_data), 1)
        col_median = round(median(column_data), 1)
        col_variance = round(variance(column_data), 1)
        col_std_dev = round(standard_deviation(column_data), 1)
        
        # Print stats 
        print(f'Attribute {col_name} ----------------')
        print(f'Mean:               {col_mean:>5}')
        print(f'Median:             {col_median:>5}')
        print(f'Variance:           {col_variance:>5}')
        print(f'Standard Deviation: {col_std_dev:>5}')
        print()  # Empty line for separation

        # Plot histograms
        plt.figure(figsize=(8, 6))
        plt.hist(column_data, bins=10, color='blue', alpha=0.5)
        plt.title(f'Histogram of attribute {col_name}')
        plt.xlabel('Value of the attribute')
        plt.ylabel('Number of data points')
        plt.grid(True)
        plt.show()

## Main function 
def main():
    # Load data
    df = load_data()
    
    # Impute missing values
    df = impute_missing_values(df)
    
    # Calculate stats and plot histograms
    calculate_stats_and_plot(df)

if __name__ == "__main__":
    main()
