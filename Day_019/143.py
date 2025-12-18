from turtle import Turtle, Screen

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
    y_axis += y_axis_factor
    turtles.append(t)

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a Color:")  

print(user_input)

screen.exitonclick()