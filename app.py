# Create a Python program that simulates a game of Rock, Paper, Scissors between the user and the computer. The program must Define the possible choices, Get the user's choice, Generate a random choice for the computer, Determine the winner based on the rules of Rock, Paper, Scissors.

# Possible Choices


import random

print("\n Welcome to rock-paper-scissors game!")

# Play function and game rules

def play():
    print("Winning rules are \n"
    + "rock vs paper = paper Wins \n"
    + "rock vs scissors = rock wins \n"
    + "paper vs scissors = scissors wins")
# game options
    options = ["rock","paper","scissors"]

# User input and computer input
    user_choice = input("choose rock or paper or scissors: ")
    computer_choice = random.choice(options)

# Print user choice and computer choice
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

# Compare choices
    if user_choice == computer_choice:
        print("Its a tie")
    elif user_choice == "rock" and computer_choice =="scissors":
        print("You wins!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

# Start game
play_game = input("press YES to start game: ")

if play_game == "YES":
    play()
else:
    print("Thanks for playing")