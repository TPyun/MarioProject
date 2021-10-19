import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1920, 1080)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shapesize(2)
    turtle.setheading(90)
    turtle.penup()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(100)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_down_curves_points(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (2*t**2 - 3*t + 1) * p1[0] + (-4*t**2 + 4*t) * p2[0] + (2*t**2 - t) * p3[0]
        y = (2*t**2 - 3*t + 1) * p1[1] + (-4*t**2 + 4*t) * p2[1] + (2*t**2 - t) * p3[1]
        draw_point((x, y))


prepare_turtle_canvas()

draw_down_curves_points((-100, 0), (0, 100), (100, 0), (-100, -50), (0, -300), (100, -50), (200, -300), (300, -50), (400, -300))


turtle.done()
