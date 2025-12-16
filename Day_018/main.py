from turtle import Turtle as t, Screen as s
import random
#with * you import everything from that module 
#from turtle import *


shelly = t()

shelly.shape("classic")
shelly.color("red")
shelly.pensize(1)
shelly.speed(0)

random_color_tuple = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# # Draw a rectangle
# for _ in range(4):
#     shelly.forward(100)
#     #shelly.color("blue")
#     shelly.right(90)

# for _ in range(15):
#     shelly.forward(10)
#     shelly.up()
#     shelly.forward(10)
#     shelly.down()

colors = ["red", "blue", "green", "gold", "purple"]

# for sides in range(3,11):
#     shelly.color(random.choice(colors))
#     for _ in range(sides):
#         shelly.forward(100)
#         shelly.right(360/sides)


screen = s()
screen.colormode(255)



def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))



def random_walk():
    random_direction = [90, 180, 270, 360]

    for _ in range(100):
        shelly.color(random_color())
        shelly.forward(25)
        shelly.setheading(random.choice(random_direction))
        #will try alternative, i dont like the movement of the turtle
        # shelly.right(random.choice(random_direction))

def spirograph(circles):
    change = 360/circles
    angle = change
    for _ in range(circles):
        shelly.color(random_color())
        shelly.circle(200)
        shelly.setheading(angle)
        angle += change

spirograph(40)
screen.exitonclick()