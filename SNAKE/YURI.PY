from __future__ import print_function, division
import turtle
import math

# ---- arc function (replaces polygon module) ----
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# ---- petal ----
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

# ---- flower ----
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)

# ---- move without drawing ----
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

# ---- setup turtle ----
bob = turtle.Turtle()
bob.speed(0)

# ---- draw flowers ----
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

bob.hideturtle()
turtle.done()