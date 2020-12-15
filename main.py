# Maze Generator
# Rohan Deswal
# rohan.deswal22@gmail.com
import pygame
from cell import *
from random import choice

pygame.init()

display_width = 500
display_height = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

n_cols = 50
n_rows = 50

width = int(display_width/n_cols)
height = int(display_height/n_rows)

cells = []

current_i = 0
current_j = 0

for x in range(0,n_cols):
    cells.append([])
    for y in range(0,n_rows):
        cells[x].append(Cell(x*width,y*height,gameDisplay,n_cols,n_rows))

cells[current_i][current_j].visited = True
cells[current_i][current_j].current = True

stack = []
stack.append(cells[current_i][current_j])

def newCurrent(x,y):
    neighbours = []
    found = False
    if x > 0:
        if cells[x-1][y].visited == False and x > 0:
            neighbours.append((x-1,y))
            found = True
    if x < n_cols - 1:
        if cells[x+1][y].visited == False and x < n_cols-1:
            neighbours.append((x+1,y))
            found = True
    if y < n_rows - 1:
        if cells[x][y+1].visited == False and y < n_rows-1:
            neighbours.append((x,y+1))
            found = True
    if y > 0:
        if cells[x][y-1].visited == False and y > 0:
            neighbours.append((x,y-1))
            found = True
    if found == True:
        cells[x][y].current = False
    if len(neighbours) > 0:
        new = choice(neighbours)
        x1 = new[0]
        y1 = new[1]
        cells[x1][y1].current = True
        cells[x1][y1].visited = True
        if new[0] == x-1:
            cells[x][y].walls[3] = False
            cells[x1][y1].walls[1] = False
        if new[0] == x+1:
            cells[x][y].walls[1] = False
            cells[x1][y1].walls[3] = False
        if new[1] == y-1:
            cells[x][y].walls[0] = False
            cells[x1][y1].walls[2] = False
        if new[1] == y+1:
            cells[x][y].walls[2] = False
            cells[x1][y1].walls[0] = False
        stack.append(cells[x1][y1])
        return x1,y1
    else:
        cells[x][y].stuck = True
        return x,y

def game_loop():
    global current_i,cells,current_j

    crashed = False
    printed = False

    FrameRate = 60

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        gameDisplay.fill((51,51,51))

        for i in range(0,n_cols):
            for j in range(0,n_rows):
                cells[i][j].show()
        current_i,current_j = newCurrent(current_i,current_j)
        if cells[current_i][current_j].stuck == True and len(stack) > 0:
            cells[current_i][current_j].current = False
            popped = stack.pop()
            current_i = int(popped.x/(width))
            current_j = int(popped.y/(height))
            cells[current_i][current_j].current = True
        if len(stack) == 0 and not printed:
            print('DONE')
            printed = True
        pygame.display.update()
        clock.tick(FrameRate)


game_loop()
pygame.display.quit()
