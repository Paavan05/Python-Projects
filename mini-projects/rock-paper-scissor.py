import random

user_score = 0
comp_score = 0

while True:
    user_input = input("Enter rock, paper or scissor or q for exit\n").lower()
    
    options = ["rock","paper","scissor"]
    rand = random.randint(0,2)
    comp = options[rand]
    
    if user_input == "q":
        print("Thank for playing!")
        break

    if user_input not in options:
        continue
    
    print(f"Computer picked: {comp}")
    
    if user_input == "rock" and comp == "scissor":
        print("You win!")
        user_score += 1
    elif user_input == "paper" and comp == "rock":
        print("You win!")
        user_score += 1
    elif user_input == "scissor" and comp == "paper":
        print("You win!")
        user_score += 1
    elif user_input == comp:
        print("Draw!")
    else:
        print("You lose!")
        comp_score += 1
        
print(f"You won: {user_score} times.")
print(f"Computer won: {comp_score} times.")