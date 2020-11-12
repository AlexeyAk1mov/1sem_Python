import pygame
from pygame.draw import *
import math


def draw_man(screen, x, y, width, height):
    '''
    Рисует мужчину в опорной точке (x, y),
    которая находится в верхнем левом углу прямоугольника,
    описанного вокруг туловища формы эллипса.
    :param width: ширина мужчины
    :param height: высота мужчины
    '''
    ellipse(screen, COLOUR['PURPLE'], (x, y, width, height))
    face(screen, x, y, width, height)
    hands_man(screen, x, y, width, height)
    legs_man(screen, x, y, width, height)


def draw_woman(screen, x, y, width, height):
    '''
    Рисует женщину в опорной точке (x, y),
    которая находится в верхнем левом углу прямоугольника,
    описанного вокруг туловища формы треугольника.
    :param width: ширина женщины
    :param height: высота женщины
    '''
    hair_woman(screen, x, y, width, height)
    polygon(screen, COLOUR['PINK'],
            [(x + width // 2, y), (x, y + height), (x + width, y + height)])
    face(screen, x, y, width, height)
    hands_woman(screen, x, y, width, height)
    legs_woman(screen, x, y, width, height)


def hair_woman(screen, x, y, width, height):
    '''Рисует волосы относительно параметров, заданных для женщины'''
    circle(screen, COLOUR['BROWN'],
           (x + width // 2, y - height // 5), height // 4)
    rect(screen, COLOUR['BROWN'], (x + int(width * 0.08),
                                  y - height // 5, height // 2, height // 2))


def face(screen, x, y, width, height):
    '''Рисует лицо относитльно параметров, заданных для мужчины или женщины'''
    circle(screen, COLOUR['FACE_COLOUR'],
           (x + width // 2, y - height // 6), height // 5)
    eyes(screen, x, y, width, height)
    nose(screen, x, y, width, height)
    mouth(screen, x, y, width, height)


def eyes(screen, x, y, width, height):
    '''Рисует глаза относитльно параметров, заданных для мужчины или женщины'''
    EYES_PARAM = [
        (COLOUR['WHITE'], 0.33, 17),
        (COLOUR['BLACK'], 0.33, 34),
        (COLOUR['WHITE'], 0.67, 17),
        (COLOUR['BLACK'], 0.67, 34),
    ]
    for j in range(4):
        circle(screen, EYES_PARAM[j][0], (x + int(EYES_PARAM[j][1] * width),
                                          y - int(0.22 * height)), height // EYES_PARAM[j][2])


def nose(screen, x, y, width, height):
    '''Рисует нос относитльно параметров, заданных для мужчины или женщины'''
    line(screen, COLOUR['BLACK'],
         (x + width // 2, y - int(0.2 * height)), (x + width // 2, y - int(height * 0.2)), 1)


def mouth(screen, x, y, width, height):
    '''Рисует рот относитльно параметров, заданных для мужчины или женщины'''
    arc(screen, COLOUR['BLACK'],
        (x + int(0.35 * width), y - int(0.18 * height),
         int(0.3 * width), height // 6),
        1.1 * math.pi, 1.9 * math.pi, 2)


def hands_man(screen, x, y, width, height):
    '''Рисует руки относитльно параметров, заданных для мужчины'''
    HANDS_MAN_PARAM = [
        ((x + width // 5, y + height // 10),
         (x - width // 2, y + int(0.65 * height))),
        ((x + int(0.8 * width), y + height // 10),
         (x + int(1.6 * width), y + height // 2)),
    ]
    for k_m in range(2):
        line(screen, COLOUR['BLACK'], HANDS_MAN_PARAM[k_m]
             [0], HANDS_MAN_PARAM[k_m][1], 2)


def hands_woman(screen, x, y, width, height):
    '''Рисует руки относитльно параметров, заданных для женщины'''
    HANDS_WOWEN_PARAM = [
        ((x + width//5, y + height//10), (x - width // 2, y + int(0.65 * height))),
        ((x + int(0.75 * width), y + height//10),
         (x + int(1.3 * width), y + int(0.3 * height))),
        ((x + int(1.3 * width), y + int(0.3 * height)),
         (x + int(1.9 * width), y + height // 4)),
    ]
    for k_w in range(3):
        line(screen, COLOUR['BLACK'], HANDS_WOWEN_PARAM[k_w]
             [0], HANDS_WOWEN_PARAM[k_w][1], 2)


def legs_man(screen, x, y, width, height):
    '''Рисует ноги относитльно параметров, заданных для мужчины'''
    LEGS_MAN_PARAM = [
        ((x + width // 3, y + int(0.95 * height)),
         (x + width // 20, y + int(1.5 * height))),
        ((x + width // 20, y + int(1.5 * height)),
         (x - width // 4, y + int(1.5 * height) + 2)),
        ((x + 2 * width // 3, y + int(0.95 * height)),
         (x + 3 * width // 4, y + int(1.49 * height))),
        ((x + 3 * width//4, y + int(1.49 * height)),
         (x + width, y + int(1.5 * height))),
    ]
    for i_m in range(4):
        line(screen, COLOUR['BLACK'], LEGS_MAN_PARAM[i_m]
             [0], LEGS_MAN_PARAM[i_m][1], 2)


def legs_woman(screen, x, y, width, height):
    '''Рисует ноги относитльно параметров, заданных для женщины'''
    LEGS_WOMAN_PARAM = [
        ((x + width // 3, y + height), (x - width // 10, y + int(1.45 * height))),
        ((x - width // 10, y + int(1.45 * height)),
         (x - int(0.4 * width), y + int(1.45 * height))),
        ((x + int(width * 0.6), y + height),
         (x + int(width * 0.8), y + int(1.45 * height))),
        ((x + int(width * 0.8), y + int(1.45 * height)),
         (x + int(1.1 * width), y + int(1.5 * height))),
    ]
    for i_w in range(4):
        line(screen, COLOUR['BLACK'], LEGS_WOMAN_PARAM[i_w]
             [0], LEGS_WOMAN_PARAM[i_w][1], 2)


def draw_balloon(screen, colour, x, y, angle, size=80):
    '''
    Рисует воздушный шарик в опорной точке (x, y), 
    которая находится в самой нижней точке оси симметрии.
    :param colour: цвет воздушного шарика.
    :param angle: угол под которым воздушный шарик располагается к горизонту.
    :param size: размер воздушного шарика.
    '''
    x2, y2, x3, y3 = [
        int(x - size * math.cos(math.radians(angle))),
        int(y - size * math.sin(math.radians(angle))),
        int(x + size * math.cos(math.radians(180 - angle - 60))),
        int(y - size * math.sin(math.radians(180 - angle - 60))),
    ]
    polygon(screen, colour, [(x, y), (x2, y2), (x3, y3)])
    BALLOON_PARAM = [(0.25, 0.75), (0.75, 0.25)]
    for el in range(2):
        circle(screen, colour, 
               (int(BALLOON_PARAM[el][0] * x2 + BALLOON_PARAM[el][1] * x3),
               int(BALLOON_PARAM[el][0] * y2 + BALLOON_PARAM[el][1] * y3)), size // 4)


def draw_ice_cream(screen, x, y, angle, size):
    '''
    Рисует мороженное в опорной точке (x, y), 
    которая находится в самой нижней точке оси симметрии.
    :param angle: угол под которым мороженное располагается к горизонту.
    :param size: - размер мороженного.
    '''
    x2, y2, x3, y3 = [
                      int(x - size * math.cos(math.radians(angle))),
                      int(y - size * math.sin(math.radians(angle))),
                      int(x + size * math.cos(math.radians(180 - angle - 60))),
                      int(y - size * math.sin(math.radians(180 - angle - 60))),
        
    ]
    x4, y4 = [
              (x2 + x3)/2 - size//4 * math.cos(math.radians(30 + angle)),
              (y2 + y3)/2 - size//4 * math.sin(math.radians(30 + angle))
    ]
    polygon(screen, COLOUR['YELLOW'], [(x, y), (x2, y2), (x3, y3)])
    ICE_CREAM_PARAM = [(COLOUR['BROWN'], 0.25, 0.75), (COLOUR['RED'], 0.75, 0.25)]
    for el in range(2):
        circle(screen, ICE_CREAM_PARAM[el][0], 
               (int(ICE_CREAM_PARAM[el][1] * x2 + ICE_CREAM_PARAM[el][2] * x3),
               int(ICE_CREAM_PARAM[el][1] * y2 + ICE_CREAM_PARAM[el][2] * y3)), size // 4)
    circle(screen, COLOUR['WHITE'], (int(x4), int(y4)), size // 4)


pygame.init()
FPS = 60
COLOUR = {
    'GREEN': (55, 200, 113),
    'BLUE': (170, 238, 255),
    'FACE_COLOUR': (244, 227, 215),
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
# draw grass
rect(screen, COLOUR['GREEN'], (0, 0, screen_width, screen_height))
# draw sky
rect(screen, COLOUR['BLUE'], (0, 0, screen_width, screen_height // 2))

# right couple
draw_man(screen, 130, 380, 100, 170)
draw_woman(screen, 320, 360, 100, 170)

# for drawing reflected objects
new = pygame.transform.flip(screen, True, False)
screen.blit(new, (0, 0))

# left couple
draw_man(screen, 130, 380, 100, 170)
draw_woman(screen, 320, 360, 100, 170)

# left balloon
line(screen, COLOUR['BLACK'], (80, 510), (65, 300), 2)
draw_balloon(screen, COLOUR['RED'], 65, 300, 50)

# central ballon
line(screen, COLOUR['BLACK'], (screen_width // 2, 30 + screen_height //
                              2), (20 + screen_width // 2, screen_height // 4), 2)
draw_balloon(screen, COLOUR['RED'], 20 + screen_width // 2, screen_height // 4, 60, size=120)

draw_ice_cream(screen, 940, 500, 90, size=80)

# display and quit event handling
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
