import turtle

turtle.shape('turtle')
turtle.color('red')
turtle.width(3)
turtle.penup()
turtle.goto(-70,0)
turtle.pendown()

def star(n):
    turtle.left(180)
    for i in range(n):
        turtle.forward(200)
        turtle.left(180 * (1 - 1 / n))
        
star(5)
turtle.penup()
turtle.goto(70,0)
turtle.pendown()
star(11)

turtle.hideturtle()
