import random

user_wins = 0
comp_wins = 0
draws = 0

options = ["rock","paper","scissors"]

# main game loop
while True:
    user_input = input("choose rock,paper,scissors or quit to quit playing: \n").lower()
    if user_input == "quit":
        break
    if user_input not in options:
        continue
    # random generator for the computer,0=rock,1=paper,2=scissors
    computer_pick = options[random.randint(0,2)]
    print("the computer picked ",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("you win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you win!")
        user_wins += 1
    elif user_input == computer_pick:
        print("a draw")
        draws += 1
    else:
        print("computer wins")
        comp_wins += 1

print("you won ",user_wins,"times.")
print("the computer won ",comp_wins,"times.")
print("you drawed ",draws,"times.")
print("Thankyou for playing and goodbye")