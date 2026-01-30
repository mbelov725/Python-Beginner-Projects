import random

random_number = random.randint(1, 100)

attempts = 0

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        attempts += 1

        difference = abs(guess - random_number)
        
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attemps.")
            break

        if difference <= 5:
            print("Very hot")
        elif 5 < difference <= 10:
            print("Warm")
        else:
            print("Cold")
    except ValueError:
        print("Please enter a valid number")