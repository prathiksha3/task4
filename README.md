# Rock, Paper, Scissors Game
# Overview
The Enhanced Rock, Paper, Scissors Game is a command-line game where you play against the computer. The game keeps track of scores and allows you to play multiple rounds. The game will prompt you to choose between rock, paper, and scissors, and it will display the results of each round.

# Features
Play Against the Computer: Choose rock, paper, or scissors, and the computer will make a random choice.

Score Tracking: Keeps track of the number of wins for both the user and the computer.

Replay Option: Allows you to play multiple rounds or exit the game.

# How to Run the Game

Ensure Python is Installed: The game is written in Python. Ensure you have Python 3.x installed on your system.

Save the Code: Copy the code into a file named rock_paper_scissors.py.

Run the Game: Open a terminal or command prompt and navigate to the directory containing rock_paper_scissors.py. Run the game with the following command:

python rock_paper_scissors.py

Follow the Prompts: The game will prompt you to choose between rock, paper, or scissors, and it will handle the rest.

# Code Explanation

get_user_choice(): Prompts the user to input their choice and validates it. Returns a valid choice.

determine_winner(user_choice, computer_choice): Determines the result of the game based on the user's choice and the computer's choice. Returns the outcome as a string.

display_result(user_choice, computer_choice, result): Prints the choices made by the user and the computer, along with the result of the game.

play_game(): Main function to handle the game loop, including score tracking and replay option.
