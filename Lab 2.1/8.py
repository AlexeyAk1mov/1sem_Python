import turtle

turtle.shape('turtle')
lenght = 10

for i in range(40):
    turtle.forward(lenght)
    turtle.left(90)
    lenght += 10

turtle.hideturtle()
