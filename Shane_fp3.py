# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 10:49:46 2024

@author: stayl
DCSI-D590
Assignment 10
Shane_fp3.py

Phase 3 objectives: 
    Write code to calculate the individual and total error rates of the predicted 
clusters based on two arguments:
    • The predicted clusters, calculated by phase 2
    • The correct clusters, specified by the column “Class“ of the initial data set
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


# PHASE TWO CODE
#    ‘Initial’ step, using random initial centroids
#    ‘Recompute’ step, updating the centroids
#    Repeat recompute until centroids/clusters don’t change or iterated 50 times

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

## BEGIN PHASE THREE
# Calculate error rates
def calculate_error_rates(df):
    # Compute error counts and total counts
    error_24 = ((df['Class'] == 4) & (df['Predicted_Class'] == 2)).sum()
    error_42 = ((df['Class'] == 2) & (df['Predicted_Class'] == 4)).sum()
    error_all = ((df['Class'] != df['Predicted_Class'])).sum()
    
    pclass_2 = (df['Predicted_Class'] == 2).sum()
    pclass_4 = (df['Predicted_Class'] == 4).sum()
    class_all = len(df)
    
    # Compute error rates
    error_B = (error_24 / pclass_2) * 100 if pclass_2 > 0 else 0
    error_M = (error_42 / pclass_4) * 100 if pclass_4 > 0 else 0
    error_T = (error_all / class_all) * 100 if class_all > 0 else 0
    
    # Print initial error rates
    print(f"Initial error rate for benign cells (class 2): {error_B:.1f} %")
    print(f"Initial error rate for malign cells (class 4): {error_M:.1f} %")
    print(f"Initial total error rate: {error_T:.1f} %")
    
    # Check for cluster swapping
    if error_T > 50:
        print("Clusters are swapped!")
        print(f"Swapping Predicted_Class Data points in Predicted Class 2: {pclass_2}")
        print(f"Data points in Predicted Class 4: {pclass_4}")
        
        # Print data points where predictions are incorrect
        print(f"Error data points, Predicted Class 2 ({len(df[(df['Class'] == 4) & (df['Predicted_Class'] == 2)])} errors):")
        print(df[(df['Class'] == 4) & (df['Predicted_Class'] == 2)][['Scn', 'Class', 'Predicted_Class']])
        
        print(f"Error data points, Predicted Class 4 ({len(df[(df['Class'] == 2) & (df['Predicted_Class'] == 4)])} errors):")
        print(df[(df['Class'] == 2) & (df['Predicted_Class'] == 4)][['Scn', 'Class', 'Predicted_Class']])
        
        # Swap clusters
        df['Predicted_Class'] = df['Predicted_Class'].replace({2: 4, 4: 2})
        
        # Recalculate error rates after swapping
        error_24 = ((df['Class'] == 4) & (df['Predicted_Class'] == 2)).sum()
        error_42 = ((df['Class'] == 2) & (df['Predicted_Class'] == 4)).sum()
        error_all = ((df['Class'] != df['Predicted_Class'])).sum()
        
        pclass_2 = (df['Predicted_Class'] == 2).sum()
        pclass_4 = (df['Predicted_Class'] == 4).sum()
        
        error_B = (error_24 / pclass_2) * 100 if pclass_2 > 0 else 0
        error_M = (error_42 / pclass_4) * 100 if pclass_4 > 0 else 0
        error_T = (error_all / class_all) * 100 if class_all > 0 else 0
        
        print(f"After swapping:")
        print(f"Error rate for benign cells (class 2): {error_B:.1f} %")
        print(f"Error rate for malign cells (class 4): {error_M:.1f} %")
        print(f"Total error rate: {error_T:.1f} %")
        
    else:
        print("Clusters are not swapped.")

def main():
    # Load data
    df = load_data()
    
    # Impute missing values
    df = impute_missing_values(df)
    
    # Phase 1: Calculate stats and plot histograms
    calculate_stats_and_plot(df)
    
    # Phase 2: K-means algorithm
    df = k_means(df)
    
    # Phase 3: Calculate error rates
    calculate_error_rates(df)
    
    # Print the first 20 data points with cluster assignments
    print("Final cluster assignment:")
    print(df[['Scn', 'Class', 'Predicted_Class']].head(20))

if __name__ == "__main__":
    main()