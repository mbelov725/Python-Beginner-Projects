import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"
emojis = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice, user_score, computer_score):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")
        user_score += 1
    else:
        print("You lose")
        computer_score += 1

    return user_score, computer_score

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        user_score, computer_score = determine_winner(user_choice, computer_choice, user_score, computer_score)

        print(f"Score: You {user_score} - {computer_score} Computer")

        should_continue = input("Continue? (y/n): ").lower()

        if should_continue == "n":
            print("Thank you for playing!")
            break

play_game()