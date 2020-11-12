import turtle

def circle():
    turtle.circle(r)
    turtle.circle(-r)

turtle.shape('turtle')
r = 100
for k in range(3):
    circle()
    turtle.left(60)
turtle.hideturtle()
