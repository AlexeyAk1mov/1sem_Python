import pygame 
from pygame.draw import *
import math


def draw_man(screen, x, y, width, height):
    '''
    Рисует мужчину в опорной точке (x, y),
    которая находится в верхнем левом углу прямоугольника,
    описанного вокруг туловища формы эллипса.
    Параметр width - ширина мужчины.
    Параметр height - высота мужчины.
    '''
    ellipse(screen, COLOR['PURPLE'], (x, y, width, height))
    face(screen, x, y, width, height)
    hands_man(screen, x, y, width, height)
    legs_man(screen, x, y, width, height)


def draw_woman(screen, x, y, width, height):
    '''
    Рисует женщину в опорной точке (x, y),
    которая находится в верхнем левом углу прямоугольника,
    описанного вокруг туловища формы треугольника.
    Параметр width - ширина женщины.
    Параметр height - высота женщины.
    '''
    hair_woman(screen, x, y, width, height) 
    polygon(screen, COLOR['PINK'],
            [(x + width // 2, y), (x, y + height), (x + width, y + height)])       
    face(screen, x, y, width, height)
    hands_woman(screen, x, y, width, height)
    legs_woman(screen, x, y, width, height)

    
def hair_woman(screen, x, y, width, height):
    '''Рисует волосы относительно параметров, заданных для женщины'''
    circle(screen, COLOR['BROWN'], (x + width // 2, y - height // 5), height // 4)
    rect(screen, COLOR['BROWN'], (x + int(width * 0.08), y - height // 5, height // 2, height // 2))


def face(screen, x, y, width, height):
    '''Рисует лицо относитльно параметров, заданных для мужчины или женщины'''
    circle(screen, COLOR['FACE_COLOR'], (x + width // 2, y - height // 6), height // 5)
    eyes(screen, x, y, width, height)
    nose(screen, x, y, width, height)
    mouth(screen, x, y, width, height)


def eyes(screen, x, y, width, height):
    '''Рисует глаза относитльно параметров, заданных для мужчины или женщины'''
    eyes_param = [
                  (COLOR['WHITE'], 0.33, 17),
                  (COLOR['BLACK'], 0.33, 34),
                  (COLOR['WHITE'], 0.67, 17),
                  (COLOR['BLACK'], 0.67, 34),
                  ]
    for j in range(4):
        circle(screen, eyes_param[j][0] , (x + int(eyes_param[j][1] * width),
            y - int(0.22 * height)), height // eyes_param[j][2])            
        

def nose(screen, x, y, width, height):
    '''Рисует нос относитльно параметров, заданных для мужчины или женщины'''
    line(screen, COLOR['BLACK'], 
        (x + width // 2, y - int(0.2 * height)), (x + width // 2, y - int(height * 0.2)), 1)
    

def mouth(screen, x, y, width, height):
    '''Рисует рот относитльно параметров, заданных для мужчины или женщины'''
    arc(screen, COLOR['BLACK'], 
        (x + int(0.35 * width), y - int(0.18 * height), int(0.3 * width), height // 6), 
        1.1 * math.pi, 1.9 * math.pi, 2)
    

def hands_man(screen, x, y, width, height):
    '''Рисует руки относитльно параметров, заданных для мужчины'''
    hands_man_param = [
                       ((x + width // 5, y + height // 10), (x - width // 2, y + int(0.65 * height))),
                       ((x + int(0.8 * width), y + height // 10), (x + int(1.6 * width), y + height // 2)),
                       ]
    for k_m in range(2):
        line(screen, COLOR['BLACK'], hands_man_param[k_m][0], hands_man_param[k_m][1], 2)

    
def hands_woman(screen, x, y, width, height):
    '''Рисует руки относитльно параметров, заданных для женщины'''
    hands_woman_param = [
                         ((x + width//5, y + height//10), (x - width // 2, y + int(0.65 * height))),
                         ((x + int(0.75 * width), y + height//10), (x + int(1.3 * width), y + int(0.3 * height))),
                         ((x + int(1.3 * width), y + int(0.3 * height)), (x + int(1.9 * width), y + height // 4)),
                         ]
    for k_w in range(3):
        line(screen, COLOR['BLACK'], hands_woman_param[k_w][0], hands_woman_param[k_w][1], 2)

    
def legs_man(screen, x, y, width, height):
    '''Рисует ноги относитльно параметров, заданных для мужчины'''
    legs_man_param = [
                      ((x + width // 3, y + int(0.95 * height)), (x + width // 20, y + int(1.5 * height))),
                      ((x + width // 20, y + int(1.5 * height)), (x - width // 4, y + int(1.5 * height) + 2)),
                      ((x + 2 * width // 3, y + int(0.95 * height)), (x + 3 * width // 4, y + int(1.49 * height))),
                      ((x + 3 * width//4, y + int(1.49 * height)), (x + width, y + int(1.5 * height))),
                      ]
    for i_m in range(4):
        line(screen, COLOR['BLACK'], legs_man_param[i_m][0], legs_man_param[i_m][1], 2)

    
def legs_woman(screen, x, y, width, height):
    '''Рисует ноги относитльно параметров, заданных для женщины'''
    legs_woman_param = [
                        ((x + width // 3, y + height), (x - width // 10, y + int(1.45 * height))),
                        ((x - width // 10, y + int(1.45 * height)), (x - int(0.4 * width), y + int(1.45 * height))),
                        ((x + int(width * 0.6), y + height), (x + int(width * 0.8), y + int(1.45 * height))),
                        ((x + int(width * 0.8), y + int(1.45 * height)), (x + int(1.1 * width), y + int(1.5 * height))),
                        ]
    for i_w in range(4):
        line(screen, COLOR['BLACK'], legs_woman_param[i_w][0], legs_woman_param[i_w][1], 2)
    
    
def balloons(screen, x, y, angle, size=80):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(screen, COLOR['RED'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(screen, COLOR['RED'], (int(0.25*x2 + 0.75*x3), int(0.25*y2 + 0.75*y3)), size//4)
    circle(screen, COLOR['RED'], (int(0.75*x2 + 0.25*x3), int(0.75*y2 + 0.25*y3)), size//4)


def ice_cream(screen, x, y, angle, size):
    x2 = int(x - size * math.cos(math.radians(angle)))
    y2 = int(y - size * math.sin(math.radians(angle)))
    x3 = int(x + size * math.cos(math.radians(180 - angle - 60)))
    y3 = int(y - size * math.sin(math.radians(180 - angle - 60)))
    polygon(screen, COLOR['YELLOW'],
            [(x, y), (x2, y2), (x3, y3)])
    circle(screen, COLOR['BROWN'], (int(0.25 * x2 + 0.75 * x3), int(0.25 * y2 + 0.75 * y3)), size//4)
    circle(screen, COLOR['RED'], (int(0.75 * x2 + 0.25 * x3), int(0.75 * y2 + 0.25 * y3)), size//4)
    x_white = (x2 + x3)/2 - size//4 * math.cos(math.radians(30+angle))
    y_white = (y2 + y3)/2 - size//4 * math.sin(math.radians(30+angle))
    circle(screen, COLOR['WHITE'], (int(x_white), int(y_white)), size//4)


pygame.init()
FPS = 60
COLOR = {
    'GREEN': (55, 200, 113),
    'BLUE': (170, 238, 255),
    'FACE_COLOR': (244, 227, 215),
    'PINK': (255, 85, 221),
    'PURPLE': (167, 147, 172),
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'BROWN': (85, 0, 0),
    'YELLOW': (255, 204, 0),
    'BLACK': (0, 0, 0),
}
screen_width, screen_height = 1032, 768

screen = pygame.display.set_mode((screen_width, screen_height))
#draw grass
rect(screen, COLOR['GREEN'], (0, 0, screen_width, screen_height))
# draw sky
rect(screen, COLOR['BLUE'], (0, 0, screen_width, screen_height // 2))

# right couple
draw_man(screen, 130, 380, 100, 170)
draw_woman(screen, 320, 360, 100, 170)

#for drawing reflected objects
new = pygame.transform.flip(screen, True, False)
screen.blit(new, (0, 0))
# left couple
draw_man(screen, 130, 380, 100, 170)
draw_woman(screen, 320, 360, 100, 170)

line(screen, COLOR['BLACK'], (80, 510), (65, 300), 2)
balloons(screen, 65, 300, 50)

line(screen, COLOR['BLACK'], (screen_width// 2, 30 + screen_height// 2), (20 + screen_width// 2, screen_height// 4), 2)
balloons(screen, 20 + screen_width// 2, screen_height// 4, 60, size = 120)

ice_cream(screen, 940, 500, 90, size = 80)

# display and quit event handling
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()