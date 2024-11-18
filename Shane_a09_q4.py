# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:12:50 2024

@author: stayl

DCSI-D590
Assignment 9
Shane_a09_q4.py

Write a Python program that uses NumPy to calculate and print average score for 
each assignment.
"""

import numpy as np

# Load the scores from the 'scores.npy' file
scores = np.load('scores.npy')

# Total the number of students based on number of rowss
num_students = scores.shape[0]

# Extract assignment columns (except id)
assign_scores = scores[:, 1:]

# Calculate the sum of scores for each  column
sum_scores = np.sum(assign_scores, axis=0)

# Calculate the average for each column
avg_scores = sum_scores / num_students

# Assignment names and corresponding indices in the average_scores array
assignments = [
    ("Homework 0", 0),
    ("Homework 1", 1),
    ("Homework 2", 2),
    ("Homework 3", 3),
    ("Homework 4", 4),
    ("Homework 5", 5),
    ("Lab 1", 6),
    ("Lab 2", 7),
    ("Lab 3", 8),
    ("Lab 4", 9),
    ("Lab 5", 10),
    ("Lab 6", 11),
    ("Lab 7", 12),
    ("Lab 8", 13),
    ("Lab 9", 14),
    ("Lab 10", 15),
    ("Lab 11", 16),
    ("Quiz 1", 19),
    ("Quiz 2", 20),
    ("Quiz 3", 21),
    ("Quiz 5", 22),
    ("Quiz 6", 23),
    ("Quiz 7", 24),
    ("Quiz 8", 25),
    ("Quiz 9", 26),
    ("Quiz 10", 27),
    ("Final project", 17),
    ("Midterm 1", 18),
    ("Midterm 2", 28)]

# Print the average scores for each assignment formatted as specified
for assignment, index in assignments:
    print(f"{assignment} average: {avg_scores[index]:.1f}")
 

