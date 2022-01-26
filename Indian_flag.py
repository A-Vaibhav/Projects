import turtle
from turtle import*

# screen to display flag
screen = turtle.Screen()
screen.setup(1300,768)

# turtle object
t = turtle.Turtle()
speed(0)

# starting point
t.penup()
t.goto(-600, 300)
t.pendown()

# Orange Rectangle
t.color("orange")
t.begin_fill()
t.forward(1200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(1200)
t.end_fill()
t.penup()
t.left(90)
t.forward(200)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(1200)
t.left(90)
t.forward(200)
t.end_fill()
t.penup()

# Blue Circle
t.goto(100,0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(100)
t.end_fill()
t.penup()

# white circle to make a blue ring
t.goto(90,0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(90)
t.end_fill()
t.penup()

# inner small blue circle
t.goto(20, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()

t.goto(-84,-12)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(6)
    t.end_fill()
    t.penup()
    t.forward(22)
    t.right(15)
    t.pendown()

t.penup()
t.goto(0,0)
t.color("navy")
t.pendown()
for i in range(24):
    t.pensize(3)
    t.forward(90)
    t.backward(90)
    t.left(15)

turtle.done()