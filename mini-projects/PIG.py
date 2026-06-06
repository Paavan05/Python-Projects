import random

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value

while True:
    players = input("Enter number of Players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 - 4")
    else:
        print("Invalid input.")
        
max_score = 50
player_scores = [0 for _ in range(players)] 

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1} turn has just started!")
        print(f"Your total score is {player_scores[player_idx]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)?").lower()
            if should_roll != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1. Turn Done!")
                current_score = 0
                break
            
            current_score += value
            print(f"You rolled {value}")
            print(f"You current score is {current_score}!")
            
        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])
        
score_max = max(player_scores)
winning_idx = player_scores.index(score_max)
print(f"Player number {winning_idx+1} is winner with a score of {score_max}")