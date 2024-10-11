import random

def get_user_choice():
    print("Enter Your Choice: rock, paper, or scissor");
    user_choice = input().lower()
    while user_choice not in ["rock", "peper", "scissor"]:
        print("Invalid choice. Enter rock, paper, or scissor.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return "rock"

def get_winner(user_choice, computer_choice):
    if computer_choice = user_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "User is the winner!" if computer_choice == "scissor" else "Computer is the winner!"
    elif user_choice == "paper":
        return "User is the winner!" if computer_choice == "rock" else "Computer is the winner!"
    elif user_choice == "scissor":
        return "User is the winner!" if computer_choice == "peper" else "Computer is the winner!"

def main():
    print("Welcome to Rock, Paper, Scissor Game");
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Your choice:", user_choice)
    print("Computer's choice:"+ computer_choice)
    result = get_winner(user_choice, computer_choice)
    print("Result:", result)

play_again = "y"
while play_again = "y":
    main()
    play_again = input("Do you want to play again? (y/n): ").lower()
    while play_again not in ["y", "n"]:
        play_again = input("Invalid input. Do you want to play again? (y/n): ").lower()

print("Thanks for playing!")
