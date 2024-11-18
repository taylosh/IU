# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:10:52 2024

@author: stayl
DCSI-D590
Assignment 10
Shane_fp2.py

Phase 2 objectives: 
    Write code for ‘Initial’ step, using numpy random to select points from data
as the initial centroids. Give first centroid name 𝜇2 and second centroid name 𝜇4.
    Write code for ‘Assign’ step, computing Euclidian distance from the two initial 
centroids in the first iteration. Store the information on predicted clusters 
into a column Predicted_Class.
    Write code for ‘Recompute’ step, updating the centroids. by computing the mean 
from the two cluster data points. 
    Iterate steps b and c until centroids/clusters don’t change or steps b and c 
iterated 50 times. Print final values of the centroids and predicted clusters.
"""

# PHASE ONE CODE
#    Load dataset 
#    Impute missing value 
#    Find the mean, median, standard deviation and variance
#    Plot histograms with 10 bins for attributes A2 to A10 (nine histograms)
    
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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


# Phase 2 CODE

# Randomly choose initial centroids
def initialize_centroids(df):
    random_indices = np.random.choice(df.index, 2, replace=False)
    mu_2 = df.loc[random_indices[0], "A2":"A10"]
    mu_4 = df.loc[random_indices[1], "A2":"A10"]
    print(f"Randomly selected row {random_indices[0]} for centroid mu_2.")
    print(f"Initial centroid mu_2:\n{mu_2}\n")
    print(f"Randomly selected row {random_indices[1]} for centroid mu_4.")
    print(f"Initial centroid mu_4:\n{mu_4}\n")
    return mu_2, mu_4

# Assign data points to nearest centroid
def assign_clusters(df, mu_2, mu_4):
    # np.linalg.norm() finds Euclidean distance
    distances_to_mu_2 = np.linalg.norm(df.loc[:, "A2":"A10"] - mu_2, axis=1)
    distances_to_mu_4 = np.linalg.norm(df.loc[:, "A2":"A10"] - mu_4, axis=1)
    # assign to 'Predicted_Class' column based on distances calculated
    df['Predicted_Class'] = np.where(distances_to_mu_2 < distances_to_mu_4, 2, 4)

# Recompute centroids based on current cluster assignments
def recompute_centroids(df):
    mu_2 = df[df['Predicted_Class'] == 2].loc[:, "A2":"A10"].mean()
    mu_4 = df[df['Predicted_Class'] == 4].loc[:, "A2":"A10"].mean()
    return mu_2, mu_4

# K-means algorithm
def k_means(df):
    mu_2, mu_4 = initialize_centroids(df)
    for iteration in range(50):
        assign_clusters(df, mu_2, mu_4)
        new_mu_2, new_mu_4 = recompute_centroids(df)
        if mu_2.equals(new_mu_2) and mu_4.equals(new_mu_4):
            print(f"Program ended after {iteration + 1} iterations.")
            break
        mu_2, mu_4 = new_mu_2, new_mu_4
    else:
        print("Program ended after 50 iterations.")

    print(f"Final centroid mu_2:\n{mu_2}\n")
    print(f"Final centroid mu_4:\n{mu_4}\n")
    return df


def main():
    # Load data
    df = load_data()
    
    # Impute missing values
    df = impute_missing_values(df)
    
    # Phase 1: Calculate stats and plot histograms
    calculate_stats_and_plot(df)
    
    # Phase 2: K-means algorithm
    df = k_means(df)
    
    # Print the first 20 data points with cluster assignments
    print("Final cluster assignment:")
    print(df[['Scn', 'Class', 'Predicted_Class']].head(20))

if __name__ == "__main__":
    main()