import random

upper_limit = 0
max_attempts = 0

while True:
    level = input("Chose your level (easy, medium, hard): ")

    if level.lower() == "easy":
        upper_limit = 50
        max_attempts = 10

        break
    elif level.lower() == "medium":
        upper_limit = 100
        max_attempts = 7

        break
    elif level.lower() == "hard":
        upper_limit = 500
        max_attempts = 8

        break

random_number = random.randint(1, upper_limit)
number_of_attempts = 0

while True:
    try:
        if number_of_attempts == max_attempts:
            print(f"Sorry, you ran out of attempts. The correct number was {random_number}")

            break

        print(f"You have {max_attempts - number_of_attempts} attempts.")
        guess = int(input(f"Guess the number between 1 and {upper_limit}: "))

        if guess < 1 or guess > upper_limit:
            print(f"Please enter a number between 1 and {upper_limit}")

            continue

        number_of_attempts += 1

        difference = abs(guess - random_number)
        
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            break

        if difference <= 5:
            print("Very hot")
        elif 5 < difference <= 10:
            print("Warm")
        else:
            print("Cold")
    except ValueError:
        print("Please enter a valid number")