import turtle
turtle.shape('turtle')
r = 100
def circle():
    turtle.circle(r)
    turtle.circle(-r)
for k in range(3):
    circle()
    turtle.left(60)
turtle.hideturtle()
