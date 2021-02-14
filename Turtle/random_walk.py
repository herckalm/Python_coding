from turtle import Screen, Turtle
import random

movements = ["forward", "backward", "right", "left"]

my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.speed(7)
my_turtle.shapesize(0.25, 0.25, 0.25)
my_turtle.pensize(15)
my_screen = Screen()
my_screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for _ in range(200):
    move = random.choice(movements)
    my_turtle.pencolor(random_color())
    if move == "forward":
        my_turtle.forward(30)
        continue
    elif move == "backward":
        my_turtle.backward(30)
        continue
    elif move == "right":
        my_turtle.right(90)
        my_turtle.forward(30)
        continue
    elif move == "left":
        my_turtle.left(90)
        my_turtle.backward(30)
        continue
