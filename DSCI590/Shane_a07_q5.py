# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 12:30:36 2024

@author: stayl

DCSI-D590
Assignment 7
Shane_a07_q5.py

Write function point() that prompts the user for a player who wins a point and 
returns “A” if player A wins, “B” if player B wins, and ”Q” if the user quits the 
game.
Write function game() that keeps the score in the game and prints the winner of 
the game.
Write function display() that prints the current score in accordance with tennis 
rules for a game.
Function main() just calls function game().
"""

def point():
    user_input = input("Who wins a point, player A or player B? ").upper()
    
    if user_input == "A":
        return "A"
    elif user_input == "B":
        return "B"
    elif user_input == "Q":
        return "Q"
    else:
        print("Invalid input. Please enter A, B or Q (to quit).")


def game():
    score_A = 0
    score_B = 0
    
    while True:
        result = point()
        
        if result == "A":
            score_A += 1
        elif result == "B":
            score_B += 1
        elif result == "Q":
            print("You quit the game.")
            return
        
        display(score_A, score_B)
        
        if score_A >= 4 and score_A >= score_B + 2:
            print("Player A wins the game.")
            return
        elif score_B >= 4 and score_B >= score_A + 2:
            print("Player B wins the game.")
            return

def display(score_A, score_B):

    tennis_score = ["0", "15", "30", "40"]
    
    if score_A <= 3 and score_B <= 3:
        print(f"Score of Player A: {tennis_score[score_A]}")
        print(f"Score of Player B: {tennis_score[score_B]}")
    elif score_A == score_B:
        print("Score of Player A: Deuce")
        print("Score of Player B: Deuce")
    elif score_A > score_B:
        if score_A - score_B == 1:
            print("Score of Player A: Adv")
            print("Score of Player B: ")
        else:
            print(f"Score of Player A: {tennis_score[score_A]}")
            print(f"Score of Player B: {tennis_score[score_B]}")
    else:
        if score_B - score_A == 1:
            print("Score of Player A: ")
            print("Score of Player B: Adv")
        else:
            print(f"Score of Player A: {tennis_score[score_A]}")
            print(f"Score of Player B: {tennis_score[score_B]}")

def main():
    print("The program keeps score and prints winner in a tennis game.")
    game()

if __name__ == "__main__":
    main()
