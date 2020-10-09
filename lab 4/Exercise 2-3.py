import numpy as np
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 255, 255)
BLUE = (0, 0, 153)
BROWN = (102, 51, 0)
DARK = (0,0,0)
WHITE = (255, 255, 255)
RED = (204, 0, 0)
LIGHT_GRAY = (204, 204, 204)
scr = pygame.display.set_mode((1500, 750))



rect(scr, LIGHT_BLUE, (0, 0, 1500, 375))
rect(scr, BLUE, (0, 375, 1500, 175))
rect(scr, YELLOW, (0, 550, 1500, 200))

#draws the sun
for j in range(37):
    c = j * np.pi / 36
    polygon(scr, YELLOW, [
                          (int(1200 + 100 * np.cos(c)), int(150 - 100 * np.sin(c))), 
                          (int(1200 + 100 * np.cos(np.pi * 2 / 3 + c)), int(150 - 100 * np.sin(np.pi * 2 / 3 + c))), 
                          (int(1200 + 100 * np.cos(np.pi * 4 / 3 + c)), int(150 - 100 * np.sin(np.pi * 4 / 3 + c)))
                          ])
#draws the shore
for i in range(15):
    circle(scr, YELLOW, (40 + 160 * i, 580), 50)
    circle(scr, BLUE, (120 + 160 * i, 520), 50)

def ship(spx, spy, sl, sw):
    polygon(scr, BROWN, [(spx, spy), (spx + sl * 4, spy), (spx + sl * 3, spy + sw), (spx, spy + sw)])
    arc(scr, BROWN, (spx - sw, spy - sw, 2 * sw, 2 * sw), np.pi, 1.5 * np.pi, sw)
    circle(scr, DARK, (spx + sl * 3, spy + int(sw / 2)), int(0.4 * sw))
    circle(scr, WHITE, (spx + sl * 3, spy + int(sw / 2)), int(0.3 * sw))
    rect(scr, DARK, (spx + sl, spy - 3 * sw, int(sl / 10), 3 * sw))
    polygon(scr, LIGHT_GRAY, [
                              (spx + sl + int(sl / 10), spy - 3 * sw),
                              (spx + int(sl * 1.2), spy - int(1.5 * sw)), 
                              (spx + sl + int(sl / 10), spy), (spx + sl * 2, spy - int(1.5 * sw))
                              ])
    polygon(scr, RED, [
                       (spx + sl, spy - 3 * sw), 
                       (spx + sl, spy - 4 * sw), 
                       (spx + int(sl * 1.5), spy - 4 * sw), 
                       (spx + int(sl * 1.3), spy - int(3.5 * sw)), 
                       (spx + int(sl * 1.5), spy - 3 * sw)
                       ])

def shipreverse(spx, spy, sl, sw):
    polygon(scr, BROWN, [(spx, spy), (spx - sl * 4, spy), (spx - sl * 3, spy + sw), (spx, spy + sw)])
    arc(scr, BROWN, (spx - sw, spy - sw, 2 * sw, 2 * sw), 1.5 * np.pi, 2 * np.pi, sw)
    circle(scr, DARK, (spx - sl * 3, spy + int(sw / 2)), int(0.4 * sw))
    circle(scr, WHITE, (spx - sl * 3, spy + int(sw / 2)), int(0.3 * sw))
    rect(scr, DARK, (spx - sl, spy - 3 * sw, int(sl / 10), 3 * sw))
    polygon(scr, LIGHT_GRAY, [
                               (spx - sl, spy - 3 * sw), 
                               (spx - int(sl * 1.2), spy - int(1.5 * sw)),
                               (spx - sl, spy),
                               (spx - sl * 2, spy - int(1.5 * sw))
                               ])
    polygon(scr, RED, [
                       (spx - int(0.9 * sl) , spy - 3 * sw),
                       (spx - int(0.9 * sl), spy - 4 * sw),
                       (spx - int(sl * 1.5), spy - 4 * sw),
                       (spx - int(sl * 1.3), spy - int(3.5 * sw)), 
                       (spx - int(sl * 1.5), spy - 3 * sw)
                       ])

def cloud(clx, cly, a, b):
    ellipse(scr, WHITE, (clx, cly, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + 2 * a, cly, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + 3 * a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + 4 * a, cly, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + 5 * a, cly - 2 * b, 4 * a, 4 * b))
    ellipse(scr, WHITE, (clx + 6 * a, cly, 4 * a, 4 * b))

def umbrella(umx, umy, ul, uw):
    rect(scr, BROWN, (umx, umy, ul * 2, uw * 3))
    polygon(scr, (204, 51, 51), [(umx + ul, umy - uw), (umx + 16 * ul, umy), (umx - 14 * ul, umy)])
    for k in range(6):
        polygon(scr, DARK, [(umx + ul, umy - uw), (umx + 16 * ul - 6 * ul * k, umy), (umx - 14 * ul, umy)], 1)

umbrella(350, 560, 10, 60)
umbrella(150, 500, 7, 50) 
cloud(200, 200, 30, 25)
cloud(900, 150, 40, 30)
ship(800, 450, 130, 60)
#Ship with two masts
shipreverse(400, 450, 50, 20)
shipreverse(600, 450, 100, 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()