from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.forward(10)

# # my_turtle.forward(200)
# # my_turtle.left(90)
# # my_turtle.forward(200)
# # my_turtle.left(90)
# # my_turtle.forward(200)
# # my_turtle.left(90)
# # my_turtle.forward(200)
# for _ in range(4):
#     my_turtle.forward(200)
#     my_turtle.left(90)

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
#


# num_sides = 5
colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]

# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     my_turtle.color(random.choice(colours))
#     draw_shape(shape_side_n)
#
# screen = Screen()
# screen.exitonclick()
# for_ in range(200):
#     my_turtle.forward(30)
#     my_turtle.setheading(random.choice(directions))
for _ in range(200):
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))




my_turtle.forward(30)
my_turtle
