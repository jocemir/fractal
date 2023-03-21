import turtle
import random

def fractal_grama(t, length, depth):
    if depth == 0:
        t.pencolor("green")
        t.forward(length)
    else:
        t.pencolor("green")
        t.forward(length/3)
        angulo = random.randint(15, 45)
        t.left(angulo)
        fractal_grama(t, length/2, depth-1)
        t.right(2*angulo)
        fractal_grama(t, length/2, depth-1)
        t.left(angulo)
        t.backward(length/3)

def desenha_grama(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.speed(0)
    fractal_grama(t, 100, 7)

t = turtle.Turtle()
desenha_grama(t, -200, -200)
desenha_grama(t, -100, -200)
desenha_grama(t, 0, -200)
desenha_grama(t, 100, -200)
desenha_grama(t, 200, -200)
turtle.done()
