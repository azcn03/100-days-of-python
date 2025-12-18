from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake_body = []
for i in range(3):
    s = Turtle(shape="square")
    s.color("white")
    s.up()
    snake_body.append(s)

x_axis = 0

for i in snake_body:
    i.teleport(x=x_axis, y=0)
    x_axis -= 20


hit_the_wall = False
# while not hit_the_wall:
#     for i in snake_body:
#         i.forward(20)
#         i.right(90)
#         if i.pos() == 0:
#             break


pos_x = 0
pos_y = 0

# def move_snake(steps, direction):

#     snake_head = snake_body[0]

#     pos_x = int(snake_head.xcor())
#     pos_y = int(snake_head.ycor())

#     snake_head.forward(20)
    
#     for i in snake_body[1:]:
#         i.teleport(pos_x, pos_y)
#         pos_x = int(i.xcor())
#         pos_y = int(i.ycor())

#     screen.update()
#     time.sleep(10)




pos_bx = 0
pos_by = 0


while not hit_the_wall:

    snake_head = snake_body[0]
    pos_x = int(snake_head.xcor())
    pos_y = int(snake_head.ycor())
    snake_head.forward(20)
    
    screen.update()
    time.sleep(3)
    
    for i in snake_body[1:]:
        pos_bx = int(i.xcor())
        pos_by = int(i.ycor())
        i.teleport(pos_x, pos_y)
        pos_x = int(i.xcor())
        pos_y = int(i.ycor())

    screen.update()
    time.sleep(1)
screen.exitonclick()


# TODO
# figure out body logic, should i solve it recursive or with a loop?
