from turtle import Turtle, Screen

shelly = Turtle()

def move_forward():
    shelly.forward(10)

screen = Screen()

screen.listen()

screen.onkey(move_forward, "d")

screen.exitonclick()