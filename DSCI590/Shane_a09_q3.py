# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 09:12:50 2024

@author: stayl

DCSI-D590
Assignment 9
Shane_a09_q3.py

Write a function “to_letter_grade(score)” that returns the letter grade for a 
scalar input “score”. See Question 1, Assignment 6, for details.
Function “main()” reads file “score_headings.npy”, calculates and prints the 
letter grade for each student.
You are supposed to use NumPy vectorized operations instead of loops.
"""

import numpy as np

# Convert score to letter grade
def to_letter_grade(score):
    if 93 <= score <= 100:
        return 'A'
    elif 90 <= score < 93:
        return 'A-'
    elif 86 <= score < 90:
        return 'B+'
    elif 83 <= score < 86:
        return 'B'
    elif 80 <= score < 83:
        return 'B-'
    elif 76 <= score < 80:
        return 'C+'
    elif 73 <= score < 76:
        return 'C'
    elif 70 <= score < 73:
        return 'C-'
    elif 66 <= score < 70:
        return 'D+'
    elif 60 <= score < 66:
        return 'D'
    else:
        return 'F'


def main():
    # Load scores 
    data = np.load('score_headings.npy')
    
    # Extract ID numbers and category scores
    ids = data[:, 0]
    cat_scores = data[:, 1:7]
    
    # Calculate the final scores 
    final_scores = np.round(np.sum(cat_scores, axis=1), decimals=1)
    
    # Convert final scores to letter 
    letter_grade_vec = np.vectorize(to_letter_grade)
    letter_grades = letter_grade_vec(final_scores)
    
    # Create array with ID numbers, scores, and letter 
    final_array = np.column_stack((ids.astype(str), final_scores.astype(str), letter_grades))
    
    # Print array as string
    for row in final_array:
        print(row)

if __name__ == "__main__":
    main()
