import colorgram
from turtle import Turtle
import random
color_list = [(199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56), (5, 57, 83), (222, 223, 226), (200, 216, 205), (108, 67, 85), (39, 36, 35), (86, 142, 58), (20, 123, 176), (110, 161, 175), (75, 39, 47), (9, 67, 47), (64, 153, 137), (133, 41, 43), (184, 98, 80), (179, 201, 186), (210, 200, 113), (179, 175, 177), (151, 176, 164), (93, 142, 156), (28, 80, 59), (194, 190, 192), (17, 78, 98), (213, 184, 173), (145, 116, 121), (176, 197, 202)]


def color_picker(image, color_width=3):
    colors = colorgram.extract(image, color_width)

    color_list = []
    for color in colors:
        my_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        color_list.append(my_tuple)

    return color_list




def paint_herst_painting(x, y, thickness, distance):
    pass

shelly = Turtle()

shelly.teleport(-325, -325)
shelly.speed(0)
shelly.screen.colormode(255)
shelly.hideturtle()

y = -325
x = -325
for i in range(10):
    for j in range(10):
        random_color = random.choice(color_list)
        shelly.dot(20, random_color)
        x += 70
        shelly.teleport(x, y)
    x = -325
    y += 70
    shelly.teleport(x, y)
    


shelly.screen.exitonclick()