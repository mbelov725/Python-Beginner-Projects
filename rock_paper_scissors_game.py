import random

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
choices = ("r", "p", "s")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")):
        print("You win!")
        user_score += 1
    else:
        print("You lose")
        computer_score += 1

    print(f"Score: You {user_score} - {computer_score} Computer")

    should_continue = input("Continue? (y/n): ").lower()

    if should_continue == "n":
        print("Thank you for playing!")
        break