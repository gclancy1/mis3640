import turtle
from turtle_shape import arc, circle, move, polygon


t = turtle.Turtle()
t.speed(0)

def draw_yinyang():
    # large circle
    circle(t, 100)

    # two arcs
    move(t, 0, 100)
    t.setheading(180)
    arc(t, 50, 180)

    move(t, 0, 100)
    t.setheading(0)
    arc(t, 50, 180)

    # small circles
    move(t, 0, 50 + 100 / 6)
    circle(t, 100 / 6)

    move(t, 0, 150 + 100 / 6)
    circle(t, 100 / 6)


draw_yinyang()
turtle.mainloop()
