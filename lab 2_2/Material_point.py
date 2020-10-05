import turtle
import math

turtle.speed(10)
turtle.shape('circle')
turtle.goto(600, 0)
turtle.goto(-600, 0)

#start of movement
x = -420
y = 0
turtle.up()
turtle.goto(x, y)
turtle.down()

#basic parameters
v_0 = 50
angle = 45
dt = 0.05
k = 0.02
g = -9.8 


v_x = v_0 * math.cos(angle)
v_y = v_0 * math.sin(angle)



while not(v_y < 0 and y < 0):
    x += v_x * dt
    y += v_y * dt
    turtle.goto(x, y)
    if y < 0:
        v_y = 0.9 * abs(v_y)
    v_y += (g - k * v_y) * dt  
    v_x -= k * v_x * dt