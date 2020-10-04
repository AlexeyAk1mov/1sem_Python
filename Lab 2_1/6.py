import turtle

turtle.shape('turtle')

for step in range(12):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360 / 12)

turtle.hideturtle()

