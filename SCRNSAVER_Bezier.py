# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 21:26:43 2022

@author: WLDru
"""

import pygame as pg
import random as rand
import sys


pg.init()

#%% Constants

black = (0, 0, 0)
white = (255, 255, 255)
dark_grey = (25, 25, 25)
light_grey = (150, 150, 150)
top = (125, 125, 125)
bottom = (75, 75, 75)
grey = (100, 100, 100)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
orange = (200, 100, 0)
blue = (0, 0, 255)

W = 1920
H = 1080


#%% setup

screen = pg.display.set_mode((W, H))

clock = pg.time.Clock()

run = True


#%% variables

animate = False

random = False

loop = False

res = 300
r = 0

#%% points

points = []

curve = []

        
#%% Actions



#%% While loop

while run:
    
    n = len(points)
    
#%% Events

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
            if event.key == pg.K_RETURN:
                if n > 2:
                    animate = True
                    curve = []
            if event.key == pg.K_BACKSPACE:
                animate = False
            if event.key == pg.K_DELETE:
                if not animate:
                    points = []
                    curve = []
            if event.key == pg.K_r:
                if not animate:
                    random = True
                    points = []
                    curve = []
            if event.key == pg.K_l:
                if not animate:
                    loop = True
                    points = []
                    curve = []
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pg.mouse.get_pos()
                points.append([x, y])              
    
    n = len(points)
    

#%% Random Drawing

    if random:
        randcount = rand.randint(5, 30)
        for i in range(randcount):
            points.append([rand.randint(0, W-1), rand.randint(0, H-1)])
            if i == randcount-1:
                random = False
                
    n = len(points)
    
#%% Animation

    if animate:
        
        if r < res:
            r += 1
        
            lines = []
            lines.append(points)
            
            for i in range(n-1, 0, -1):
                if i == 1:
                    curve.append([int((r/res)*(lines[-1][-1][0]-lines[-1][-2][0])+lines[-1][-2][0]),
                                  int((r/res)*(lines[-1][-1][1]-lines[-1][-2][1])+lines[-1][-2][1])])
                else:
                    line = []
                    for j in range(i):
                        line.append([((r/res)*(lines[-1][j+1][0] - lines[-1][j][0])) + lines[-1][j][0], 
                                     ((r/res)*(lines[-1][j+1][1] - lines[-1][j][1])) + lines[-1][j][1]])
                    lines.append(line)
                
            
            for i, sequence in enumerate(lines):
                for j, point in enumerate(sequence):
                    lines[i][j][0] = int(lines[i][j][0])
                    lines[i][j][1] = int(lines[i][j][1])
        
        else:
            animate = False
            r = 0
    
                
#%% Drawing to Screen

    screen.fill(black) 
    
    if n == 1:
        pg.draw.circle(screen, light_grey, points[0], 5)
    if n > 1:
        pg.draw.lines(screen, light_grey, False, points,  1)
        pg.draw.circle(screen, light_grey, points[0], 5)
        for point in points:
            pg.draw.circle(screen, light_grey, point, 5)
    
    if animate:
        for s, sequence in enumerate(lines):
            color = ((((s+1)/n)*255), (((s+1)/n)*255), (((s+1)/n)*255))
            if s != 0:
                pg.draw.lines(screen, color, False, sequence, 1)
    if len(curve) > 1:
        pg.draw.lines(screen, red, False, curve, 3)
        

#%% Loop

    if loop:
        if not animate:
            random = True
            animate = True
            points = []
            curve = []
        
                
#%% Update Frame

    pg.display.update()
    clock.tick(60)

#%% Exit Statement

pg.quit()
sys.exit()