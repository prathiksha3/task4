import random
def get_user_choice():
    valid_choices = ['rock', 'paper', 'scissors']
    prompt = f"Choose {', '.join(valid_choices)}: "

    while True:
        user_choice = input(prompt).lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print("Invalid choice. Please choose a valid option.")

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('rock', 'scissors'): 'You win!',
        ('scissors', 'paper'): 'You win!',
        ('paper', 'rock'): 'You win!',
        ('scissors', 'rock'): 'You lose!',
        ('paper', 'scissors'): 'You lose!',
        ('rock', 'paper'): 'You lose!',
    }
    
    if user_choice == computer_choice:
        return "It's a tie!"
    else:
        return outcomes.get((user_choice, computer_choice), "Invalid input.")

def display_result(user_choice, computer_choice, result):
    print(f"You chose {user_choice}. The computer chose {computer_choice}. {result}")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if 'win' in result:
            user_score += 1
        elif 'lose' in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to the Enhanced Rock, Paper, Scissors Game!")
    play_game()
