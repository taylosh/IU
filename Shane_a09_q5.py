# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:12:50 2024

@author: stayl

DCSI-D590
Assignment 9
Shane_a09_q5.py

Write a Python program that uses NumPy to calculate and print average of each 
assignment group.
"""

import numpy as np

# Load the scores 
scores = np.load('scores.npy')

# Extract columns (excluding id)
assign_scores = scores[:, 1:]

# Get number of students
num_students = scores.shape[0]

# Calculate averages for each group
# Homework: columns HW 0 to HW 5 (indices 0 to 5)
homework_sum = np.sum(assign_scores[:, 0:6], axis=0)
homework_avg = homework_sum / num_students

# Labs: columns Lab 01 to Lab 11 (indices 6 to 16)
labs_sum = np.sum(assign_scores[:, 6:17], axis=0)
lab_avg = labs_sum / num_students

# Final Project: column Final Project (index 17)
final_project_sum = np.sum(assign_scores[:, 17])
final_project_avg = final_project_sum / num_students

# Midterm 1: column Midterm 1 (index 18)
midterm1_sum = np.sum(assign_scores[:, 18])
midterm1_avg = midterm1_sum / num_students

# Quizzes: columns Quiz 01 to Quiz 10 !!ONLY 9!! (indices 19 to 28)
quizzes_sum = np.sum(assign_scores[:, 19:28], axis=0)
quiz_avg = quizzes_sum / num_students

# Midterm 2: column Midterm 2 (index 28)
midterm2_sum = np.sum(assign_scores[:, 28])
midterm2_avg = midterm2_sum / num_students

# Condense multi-assignment arrays to cat total
num_homeworks = 6
num_labs = 11
num_quizzes = 9

tot_homework_avg = np.sum(homework_avg) / num_homeworks
tot_lab_avg = np.sum(lab_avg) / num_labs
tot_quiz_avg = np.sum(quiz_avg) / num_quizzes

# Print the averages rounded to 1 decimal 
print(f"Homework average: {tot_homework_avg:.1f}")
print(f"Lab average: {tot_lab_avg:.1f}")
print(f"Quiz average: {tot_quiz_avg:.1f}")
print(f"Project average: {final_project_avg:.1f}")
print(f"Midterm 1 average: {midterm1_avg:.1f}")
print(f"Midterm 2 average: {midterm2_avg:.1f}")
