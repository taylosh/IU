# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:12:50 2024

@author: stayl

DCSI-D590
Assignment 9
Shane_a09_q1.py

Open file “Scores_all.xlsx” with Excel and save it in plain text using “csv” 
format (Comma Separated Values) to file “Scores_all.csv”.

Write a Python program that uses NumPy to:
• Read “Scores_all.csv”,
• Delete the first row (with column headings),
• Fill out the missing data with 0s,
• Print the resulting data array and save it to the file “scores.npy”.
"""

import numpy as np
from numpy import genfromtxt

# Read the CSV file into a NumPy array, including headers and handling missing values as NaN
scores_all = genfromtxt("Scores_all.csv", delimiter = ",")

# Create a view that excludes the first row (with headers)
scores = scores_all[1:]

# Replace NaN values with 0
scores[np.isnan(scores)] = 0

# Convert the data type of the array to integers
scores = scores.astype(int)

# Print the resulting array to check
print(scores)

# Save the array to the file "scores.npy"
np.save('scores.npy', scores)


