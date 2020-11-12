import turtle

def moving(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_eye(size=50):
    turtle.color('blue')
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    

turtle.shape('turtle')
turtle.color('yellow')
turtle.speed(10)

moving(0, -200)
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

moving(-70, 30)
draw_eye()
moving(70, 30)
draw_eye()

moving(0, 30)
turtle.color('brown')
turtle.width(10)
turtle.right(90)
turtle.forward(60)

moving(120, 0)
turtle.color('red')
turtle.width(20)
turtle.circle(-120,180)

turtle.hideturtle()









