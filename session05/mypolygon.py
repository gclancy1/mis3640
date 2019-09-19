import turtle
import math

brian = turtle.Turtle()

brian.pensize(10)
print(brian)

# for _ in range(4):
#     brian.fd(100)
#     brian.lt(90)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360 / n)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)


# def arc(t, r, angle):
#     """
#     Draw an arc with radius, r, and angle (in degree)
#     """
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n

#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def move(t, x, y):
    t.pu()
    t.setpos(x, y)
    t.pd()


# square(brian, 200)
# polygon(brian, 8, 100)
# polygon(brian, n=8, length=100)
# circle(brian, 100)

# arc(brian, 100, 90)
arc(brian, 100, 360)
move(brian, -200, 100)
polygon(brian, 3, 100)


turtle.mainloop()
