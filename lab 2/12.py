import turtle

def more_arc():
    turtle.circle(-r, 180)
    turtle.circle(-r + 50, 180)

turtle.shape('turtle')
turtle.speed(10)
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
turtle.left(90)
r = 60
for k in range(5):
    more_arc()
turtle.circle(-r, 180)    
turtle.hideturtle()
