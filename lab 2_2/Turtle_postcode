import turtle as tr

a = 30
tr.width(3)

DIGITS = [
  [(0, a), (-90, 2 * a), (-90, a), (-90, 2 * a), (-90, 0)],
  [(45, a * 2 ** 0.5), (-135, 2 * a), (90, 0)],
  [(0, a), (-90, a), (-45, a * 2 ** 0.5), (135, a)],
  [(0, a), (-135, a * 2 ** 0.5), (135, a), (-135, a * 2 ** 0.5), (135, 0)],
  [(-90, a), (90, a), (90, a), (180, 2 * a), (90, 0)],
  [(0, a), (180, a), (90, a), (90, a), (-90, a), (-90, a), (180, 0)],
  [(-135, a * 2 ** 0.5), (135, a), (-90, a), (-90, a), (-90, a), (-90, 0)],
  [(0, a), (-135, a * 2 ** 0.5), (45, a), (90, 0)],
  [(0, a), (-90, a), (-90, a), (-90, a), (180, 2 * a), (90, a), (90, a), (-90, 0) ],
  [(0, a), (-90, a), (-45, a * 2 ** 0.5), (180, a *2 ** 0.5), (135, a), (-90, a), (-90, 0)]
  ]

def write_digit(n):
    if n == 1:
          tr.penup()
          tr.left(-90) 
          tr.forward(a)
          tr.left(90)
          tr.pendown()
    if n == 6:
          tr.penup()
          tr.forward(a)
          tr.pendown()
    for T in DIGITS[n]:
      angle, length = T
      tr.left(angle)    
      tr.forward(length)
      

postcode = list(map(int, input('Введите почтовый индекс через пробел:').split()))
indent = 40
for n in postcode:
    write_digit(n)
    tr.penup()
    tr.goto(indent, 0)
    tr.pendown()
    indent += 40

tr.hideturtle()