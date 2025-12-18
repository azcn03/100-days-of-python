from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)


turtles = []
y_axis_factor = (400 - 40)/ (len(colors) - 1) #we have a line, with n nodes so n-1 lines

y_axis = -180
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.teleport(x=-230, y=y_axis)
    t.up()
    y_axis += y_axis_factor
    turtles.append(t)

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:")  
winning_turtle = None

crossed_line = False

while not crossed_line:
    for i in turtles:
        i.forward(random.randint(1,20))
        if i.pos()[0] >= 230:
            crossed_line = True
            winning_turtle = i.color()[0]
            print()
            break  

if user_input.lower() == winning_turtle.lower():
    print("You won")
else:
    print("You lost")
    
screen.exitonclick()