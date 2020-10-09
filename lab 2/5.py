import turtle

turtle.shape('turtle')
lenght = 50
x = -10
y = -10

for i in range(10):
    for base in range(4):
        turtle.forward(lenght)
        turtle.left(90)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    lenght += 20
    x -= 10
    y -= 10

turtle.hideturtle()

