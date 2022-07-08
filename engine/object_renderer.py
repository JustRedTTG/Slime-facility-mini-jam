import pygame as pg
import engine.window as window
import engine.data as data

objects = []

class selection_popup:
    def __init__(self, action):
        self.action = action
        self.halt = True
        self.ID = action.ID
        self.frame = -1
    def render(self):
        migrade = int(window.size[0] * .1), int(window.size[1] * .1)
        borderlength = int((migrade[0] + migrade[1]) * .05)
        i = 0
        for y in range(migrade[1]+borderlength, window.size[1]-migrade[1]-borderlength):
            pg.draw.line(window.dis, data.boxart_pallet[i], (migrade[0]+borderlength, y), (window.size[0]-migrade[0]-borderlength, y))
            i += 1
            if i >= len(data.boxart_pallet): i = 0
        pg.draw.rect(window.dis, data.boxart_color, (*migrade, window.size[0]-migrade[0]*2, window.size[1]-migrade[1]*2), borderlength, int(migrade[0] * borderlength * 0.02))