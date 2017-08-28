import pygame
from pygame.locals import *
import random
import math
width = int(input("what width?"))
height = int(input("what height?"))
bombs_number = input("bombs in percent or number?")
if bombs_number == "percent":
    bombs_number = int((int(input("how many percent bombs?"))/100) * height * width)
else:
    bombs_number = int(input("how many bombs?"))


class App(object):
#The screen
    def __init__(self,width,height,bombs_number):
        self.render_check = True
        self.width = width
        self.height = height
        self.bombs_number = bombs_number
        self.size = (self.width * 50, self.height * 50)
        self.tiles = []
        self.bombs = []
        for i in range(self.height):
            self.tiles.append(["plain"])
            self.bombs.append([False])
            for i2 in range(1,self.width):
                self.tiles[i].append("plain")
                self.bombs[i].append(False)

    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        pygame.init()

    def render(self):
        if not(self.render_check):
            return
        counter_i = 0
        for i in range(len(self.tiles)):
            counter_i2 = 0
            for i2 in self.tiles[i]:
                self.screen.blit(pygame.image.load("Images/%s.png" % i2), ((50 * counter_i2), (50 * counter_i)))
                pygame.display.flip()
                counter_i2 = counter_i2 + 1
            counter_i = counter_i + 1
        self.render_check = False

    def get_mouse(self):
        while True:
            pygame.event.get()
            mouse_click = pygame.mouse.get_pressed()
            if mouse_click[0] == True or mouse_click[2] == True:
                if mouse_click[0] == True:
                    mouse_button = "left"
                else:
                    mouse_button = "right"
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = [int(mouse_pos[0]/50),int(mouse_pos[1]/50)]
                return mouse_pos,mouse_button

    def turn_tile(self,coordinates):
        bomb_count = 0
        for i in range(coordinates[0] - 1,coordinates[0] + 2):
            if i > -1 and i < self.width :
                for i2 in range(coordinates[1] - 1,coordinates[1] + 2):
                    if i2 > -1 and i2 < self.height:
                        if self.bombs[i][i2]:
                            bomb_count = bomb_count + 1
        if bomb_count == 0:
            self.tiles[coordinates[1]][coordinates[0]] = "clear"
            self.render_check = True
            return False
        else:
            self.tiles[coordinates[1]][coordinates[0]] = bomb_count
            self.render_check = True
            return True

    def action(self):
        mouse = self.get_mouse()
        if mouse[1] == "left":
            clear_tiles = self.turn_tile(mouse[0])
            uncleared_tiles = []
            while True:
                if clear_tiles == False:
                    for i in self.tiles:
                        for i2 in i:
                            if i2 == 0:
                                uncleared_tiles.append([i2,i])
                    if uncleared_tiles:
                        for i in uncleared_tiles:
                            self.turn_tile(i)
                    else:
                        clear_tiles = True
                else:
                    break


        else:
            if self.tiles[mouse[0][1]][mouse[0][0]] == "plain":
                self.tiles[mouse[0][1]][mouse[0][0]] = "flag"
                self.render_check = True

    def bomb_generation(self):
        while bombs_number > 0:
            bomb_coord = [(random.randint(0,(len(self.tiles[0]) - 1))),(random.randint(0,(len(self.tiles) - 1)))]
            if self.bombs[bomb_coord[0]][bomb_coord[1]] == False:
                self.bombs[bomb_coord[0]][bomb_coord[1]] = True
                self.bombs_number = self.bombs_number - 1



theApp = App(width,height,bombs_number)
theApp.start()
theApp.bomb_generation()


while True:
    theApp.render()
    theApp.action()
    pygame.time.delay(10)
