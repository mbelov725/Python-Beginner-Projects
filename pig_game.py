'''
This is a version of the game pig played using dice, for 2-4 players.
Each player takes turns rolling two dice to accumulate points.

If a player rolls two numbers each between 2 and 6, the sum is added to their current turn score.
If a player rolls one 1, their turn ends and they lose all points accumulated during that turn.
If a player rolls two 1s, their turn ends and their total score goes to zero.
A player may choose to stop rolling at any time, at which point their current turn score is added to their total score.

The first player to reach or exceed 100 total points wins the game.

'''

import random

def roll():
    MIN_VALUE = 1
    MAX_VALUE = 6
    
    roll_1 = random.randint(MIN_VALUE, MAX_VALUE)
    roll_2 = random.randint(MIN_VALUE, MAX_VALUE)

    return roll_1, roll_2

while True:
    players = input("Enter the number of players (2-4): ")
    
    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Must be bewteen 2-4 players")
    else:
        print("Please enter a valid number")

MAX_SCORE = 100
player_scores = [0 for _ in range(players)]

while max(player_scores) < MAX_SCORE:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll? (y): ")
            
            if should_roll.lower() != "y":
                break
            
            die_1, die_2 = roll()

            if die_1 == 1 and die_2 == 1:
                player_scores[player_idx] == 0
                current_score = 0
                print("Snake eyes! Total score reset.")
                break
            elif die_1 == 1 or die_2 == 1:
                print("You rolled a 1! Turn done")
                current_score = 0
                break
            else:
                current_score += die_1 + die_2
                print(f"You rolled a {die_1} and a {die_2}")

            print(f"Your score is: {current_score}")

        player_scores[player_idx] += current_score

        print(f"Your total score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"Player {winning_idx + 1} is the winner with a score of {max_score}!")