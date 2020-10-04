import turtle
import math

turtle.shape('turtle')
turtle.speed(0)
pi = 3.14159265
a = 20
k = a / (2 * pi)
f = 0
while f < 5 * (2 * pi):
     p = k * f
     x = p * math.cos(f)
     y = p * math.sin(f)
     turtle.goto(x,y)
     f += 0.01
turtle.hideturtle()
    
