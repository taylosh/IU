# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:03:12 2024

@author: stayl

DCSI-D590
Assignment 6
Shane_a06_q4.py

Write function point() that prompts the user for a player who wins a point and 
returns “A” if player A wins a point and returns “B” if player B wins a point.
Write function game() that keeps the score in the game and returns “A” if player 
A wins the game or “B” if player B wins the game.
Write function main() that calls the previous functions and prints the winner of 
the game.
"""

def point():
    # Prompt for the player who wins a point
    winner = input("Enter the player who wins the point (A or B): ").upper()
    if winner in ['A', 'B']:
        return winner
    else:
        print("Invalid input. Please enter 'A' or 'B'.")
        return

def game():
    # Keeps score and returns 'A' if player wins or 'B' if other player wins.
    score_A = 0
    score_B = 0
    
    for _ in range(20):  # Loop up to 20 times 
        winner = point()
        
        if winner == "A":
            score_A += 1
        elif winner == "B":
            score_B += 1
        
        print(f"Player A score: {score_A}\nPlayer B score: {score_B}")
        
        # Check if a player has won the game
        if (score_A >= 3 and score_A >= score_B + 2) or score_A == 7:
            return "A"
        elif (score_B >= 3 and score_B >= score_A + 2) or score_B == 7:
            return "B"

    # If no winner is determined after 20 points
    print("Game ended without a clear winner.")
    return None

def main():
    print("The program keeps score in a game.")
    winner = game()
    
    if winner == "A":
        print("The winner is player A!")
    elif winner == "B":
        print("The winner is player B!")

# Run the main function
if __name__ == "__main__":
    main()


