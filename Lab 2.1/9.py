import turtle
import math
turtle.shape('turtle')
n = 3
r = 10
def polygon(n, length): # функция, рисующая многоугольник
    k = 360/n
    while n > 0:
        turtle.left(k)
        turtle.forward(length)
        n -= 1
        
while n < 13:
    length = 2 * r * math.sin(math.pi / n) #считаем размер стороны многоугольника 
    alpha =(180 - 360 / n) / 2
    turtle.left(alpha)
    
    polygon(n, length)
    turtle.right(alpha)
    turtle.penup()
    turtle.forward(10)  
    turtle.pendown()
    n += 1
    r += 10 
