# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:55:18 2024

@author: stayl

DCSI-D590
Assignment 4
Shane_a04_q5.py
A program that reads a file, counts and prints the number of words in the file.
"""

def main():
    print("The program counts number of words in an input file.")

    # Function to count words by line
    def count_words(file):
        # Initialize count
        word_count = 0        
        for line in file:
        # Break up the line (string) into a list of the words
            words = line.split()
            # Add the number of words in the line (accumulating over the lines)
            word_count += len(words)
        # Return the total count
        return word_count
    
    # Take the user input
    file_name = input("Enter a file name: ")
    
    # Open the file
    file= open(file_name, 'r')

    # Execute count_words on file
    count = count_words(file)
    print("There are", count, "words in the file.")
    
main()
