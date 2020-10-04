import turtle

turtle.shape('turtle')
turtle.color('yellow')
turtle.speed(10)

turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

turtle.penup()
turtle.goto(-70, 30)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(70, 30)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.color('brown')
turtle.width(10)
turtle.right(90)
turtle.forward(60)

turtle.penup()
turtle.goto(120, 0)
turtle.pendown()
turtle.color('red')
turtle.width(20)
turtle.circle(-120,180)

turtle.hideturtle()









