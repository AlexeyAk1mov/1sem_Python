import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
r = 50
def circle():
        turtle.circle(r)
        turtle.circle(-r)
for k in range(10):
    circle()
    r += 10
turtle.hideturtle()
