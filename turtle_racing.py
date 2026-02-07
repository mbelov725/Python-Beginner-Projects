import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLOURS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "black",
    "purple",
    "pink",
    "brown",
    "cyan"
]

def get_number_of_turtles():
    MIN_NUMBER = 2
    MAX_NUMBER = 10
    turtles = 0

    while True:
        turtles = input(f"Enter the number of turtles ({MIN_NUMBER}-{MAX_NUMBER}): ")
        if turtles.isdigit():
            turtles = int(turtles)
            if MIN_NUMBER <= turtles <= MAX_NUMBER:
                return turtles
            else:
                print(f"The number of turtles must be between {MIN_NUMBER} and {MAX_NUMBER}.")
        else:
            print("Input is not numeric. Try again.")

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

def create_turtes(colours):
    turtles = []
    spacing_x = WIDTH // (len(colours) + 1)
    spacing_y = -HEIGHT//2 + 20

    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1)*spacing_x, spacing_y)
        racer.pendown()
        turtles.append(racer)

    return turtles

def race(colour):
    turtles = create_turtes(colour)
    finish_y = HEIGHT//2 - 10

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= finish_y:
                return colour[turtles.index(racer)]

def main():
    racers = get_number_of_turtles()
    init_turtle()

    random.shuffle(COLOURS)
    colours = COLOURS[:racers]

    winner = race(colours)
    print(f"The {winner} turtle is the winner!")
    time.sleep(5)

main()