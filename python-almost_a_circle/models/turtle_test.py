#!/usr/bin/python3

import turtle

screen = turtle.Screen()
screen.title("A turtle Graphics Screen")
screen.setup(600, 600)
screen.bgcolor("cyan")

skk = turtle.Turtle()

for i in range(4):
    skk.forward(50)
    skk.right(90)

turtle.done()
