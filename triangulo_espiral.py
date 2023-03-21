
import turtle

n = 10
pen = turtle.Turtle()
for i in range(n * 3):
    pen.forward(i * 10)

    pen.right(120)

turtle.done()