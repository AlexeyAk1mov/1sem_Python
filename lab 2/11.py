import turtle

def circle():
        turtle.circle(r)
        turtle.circle(-r)

turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
r = 50
for k in range(10):
    circle()
    r += 10
turtle.hideturtle()
