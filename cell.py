# Maze Generator
# Rohan Deswal
# rohan.deswal22@gmail.com
import pygame

class Cell:

    def __init__(self,x,y,display,n_cols,n_rows):
        self.x = x
        self.y = y
        self.display = display
        self.visited = False
        # top, right, bottom, left
        self.walls = [True, True, True, True]
        self.w = int(self.display.get_width()/n_cols)
        self.h = int(self.display.get_height()/n_rows)
        self.display_width = self.display.get_width()
        self.display_height = self.display.get_height()
        self.current = False
        self.stuck = False

    def show(self):
        line_color = (109,3,36)
        lw = 1
        if self.visited:
            pygame.draw.rect(self.display,(179,69,247),[self.x,self.y,self.w,self.h])
        if self.current:
            pygame.draw.rect(self.display,(249,241,77),[self.x,self.y,self.w,self.h])
        # top
        if self.walls[0]:
            pygame.draw.line(self.display,line_color,(self.x,self.y),(self.x+self.w,self.y),lw)
        # right
        if self.walls[1]:
            pygame.draw.line(self.display,line_color,(self.x+self.w,self.y),(self.x+self.w,self.y+self.h),lw)
        # bottom
        if self.walls[2]:
            pygame.draw.line(self.display,line_color,(self.x,self.y+self.h),(self.x+self.w,self.y+self.h),lw)
        # left
        if self.walls[3]:
            pygame.draw.line(self.display,line_color,(self.x,self.y+self.h),(self.x,self.y),lw)
