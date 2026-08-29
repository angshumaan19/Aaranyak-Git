import random as r
while True:
    user_action=input("enter your choice(rock,paper or scissors)")
    playable_actions=["rock","paper","scissors"]
    computer_action=r.choice(playable_actions)

    print("you chose",user_action,"computer chose",computer_action)

    if user_action == computer_action:
        print(f"its a tie, both players chose {user_action}")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
             print("Paper covers rock! You win!")
        else:
             print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
             print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
