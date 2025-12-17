from turtle import Turtle, Screen

shelly = Turtle()

def move_forward():
    shelly.forward(10)

def move_backward():
    shelly.forward(-10)

def turn_clockwise():
    shelly.right(10)

def turn_counterclockwise():
    shelly.left(10)
    
def clear_screen():
    shelly.clear()
    shelly.teleport(0,0)
    shelly.setheading(0)

screen = Screen()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "a")
screen.onkey(turn_counterclockwise, "d")
screen.onkey(clear_screen,"c")

screen.exitonclick()