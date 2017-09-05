import turtle
# Magnus Crooke, Date last modified(09/5/17), File Name: unit one project.py,
# This program makes 4 diffent octagons in 4 differnet place in4 diffenrt colors


def move_turtle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    # this function is for moving the turtle without drawing a line to its next coordinates


def draw_octagon(color):
    turtle.color(color)
    turtle.begin_fill()
    # this function is for coloring the octagon
    for x in range(8):  # this function is for drawing the octagon
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()


turtle.goto(0, 0)
draw_octagon("Red")
# End First


move_turtle(250, 0)
draw_octagon("Green")
# End Second

move_turtle(250, -250)
draw_octagon("Blue")
# End Third


move_turtle(0, -250)
draw_octagon("Purple")
# End Fourth

turtle.exitonclick()
