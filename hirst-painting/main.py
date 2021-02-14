import turtle as t
import random
import colorgram

colors = colorgram.extract('hirst.jpg', 30)
color_list = [color.rgb for color in colors]
color_list = [tuple(rgb) for rgb in color_list]

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.penup()
my_turtle.hideturtle()

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

dots = 100

for dot in range(1, dots+1):
    color = random.choice(color_list)
    my_turtle.dot(20, color)
    my_turtle.forward(50)

    if dot % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

t.Screen().exitonclick()
