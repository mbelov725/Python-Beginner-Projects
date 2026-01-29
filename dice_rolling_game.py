import random
import math


def probability(n, m):
    total = 0

    for k in range((m - n) // 6 + 1):
        sign = (-1) ** k
        ways = math.comb(n, k) * math.comb(m - 6*k - 1, n - 1)
        total += sign * ways

    return total / (6 ** n)
        

while True:
    choice = input("Roll the dice? (y/n): ")

    if choice.lower() == "y":
        while True:
            number_of_die = int(input("How many die would you like to roll? "))
            
            if number_of_die > 0:
                die_values = []
                sum = 0

                for number in range(number_of_die):
                    random_number = random.randint(1,6)

                    die_values.append(random_number)
                    sum += random_number

                print(die_values)

                print(f"The probability of rolling a sum of {sum} with {number_of_die} die is {probability(number_of_die, sum)}")

                average_sum = round(3.5 * number_of_die)

                print(f"The most likely sum is {average_sum} with a probability of {probability(number_of_die, average_sum)}")

                break
            else:
                print("You must roll at least one dice")
    elif choice.lower() == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")