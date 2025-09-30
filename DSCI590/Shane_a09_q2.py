# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:12:50 2024

@author: stayl

DCSI-D590
Assignment 9
Shane_a09_q2.py

Write a Python program that uses NumPy to read file “scores.npy” and create a 
NumPy array “score_headings” with the following columns:
• ID numbers,
• Weighted scores for the homework assignment,
• Weighted scores for the labs,
• Weighted final project scores,
• Weighted midterm 1 scores,
• Weighted scores for the quizzes,
• Weighted midterm 2 scores.
Print “score_headings” and store it to file “score_heading.npy”.
"""

import numpy as np

# Set print options to suppress scientific notation
np.set_printoptions(suppress=True)

# Load the data from "scores.npy"
scores = np.load('scores.npy')

# Check if the first row contains non-student data (e.g., max points)
if scores[0, 0] == 0:
    scores = scores[1:]
    
# Create score_headings with weighted scores
ids = scores[:, 0]

# Calculate weighted scores for each category using vectorized operations
weighted_homework = (scores[:, 1:7].sum(axis=1) / 600) * 20
weighted_labs = (scores[:, 7:18].sum(axis=1) / 1100) * 30
weighted_finalproject = (scores[:, 18] / 100) * 10
weighted_midterm1 = (scores[:, 19] / 100) * 10
weighted_quizzes = (scores[:, 20:29].sum(axis=1) / 90) * 15
weighted_midterm2 = (scores[:, 29] / 100) * 15

# Stack all the weighted scores into a single array
score_headings = np.column_stack((ids, weighted_homework, weighted_labs,
                                  weighted_finalproject, weighted_midterm1,
                                  weighted_quizzes, weighted_midterm2))

# Save the score_headings array to "score_headings.npy"
np.save('score_headings.npy', score_headings)

# Print the score_headings array to check
print(np.around(score_headings, decimals=1))