import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


t.colormode(255)
my_turtle = t.Turtle()

my_turtle.speed("fastest")
my_turtle.shapesize(0.25, 0.25, 0.25)
my_turtle.pensize(2)

for _ in range(72):
    my_turtle.pencolor(random_color())
    my_turtle.circle(100)
    my_turtle.left(5)

t.Screen().exitonclick()
