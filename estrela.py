import turtle

Screen = turtle.Turtle()
cores = ['red', 'green', 'blue', 'yellow', 'black']

turtle.pensize(15)

turtle.penup()
turtle.setpos(-90,30)
turtle.pendown()
for i in range(5):
    turtle.pencolor(cores[i])
    turtle.forward(200)
    turtle.right(144)

turtle.done()
