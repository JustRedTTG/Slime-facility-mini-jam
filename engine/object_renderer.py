import math
import pygame as pg
import engine.window as window
import engine.data as data

objects = []

def boxart(migrade,ex,ey):
    i = 0
    borderlength = int((migrade[0] + migrade[1]) * .05)
    for y in range(migrade[1] + borderlength, ey - borderlength):
        pg.draw.line(window.dis, data.boxart_pallet[i],
                     (migrade[0]+borderlength, y),
                     (ex - borderlength, y))
        i += 1
        if i >= len(data.boxart_pallet): i = 0
    pg.draw.rect(window.dis, data.boxart_color,
                 (*migrade, ex - migrade[0], ey - migrade[1]),
                 borderlength,int(migrade[0] * borderlength * 0.02))

class popup:
    def __init__(self, action):
        self.action = action
        self.halt = True
        self.ID = action.ID
        self.buildSize = tuple(window.size)
        self.font()
    def font(self):
        factor = len(self.action.title) - 10
        scale = factor * .0033
        scale = factor * scale * .026
        scale = (800 * .1 - len(self.action.title) * scale) / 1000
        scale = int(window.size[0] * scale)
        self.title = pg.font.Font('font.ttf', scale).render(self.action.title,True, data.box_text_color)
    def content(self): pass
    def render(self):
        if self.buildSize != window.size:
            self.buildSize = tuple(window.size)
            self.font()
        migrade = int(window.size[0] * .1), int(window.size[1] * .1)
        boxart(migrade, window.size[0] - migrade[0], window.size[1] - migrade[1])
        title_size = self.title.get_size()
        window.dis.blit(self.title, (window.size[0]/2 - title_size[0]/2, migrade[1]*2))

        self.content()

class loading_popup(popup):
    def content(self):
        pass
class selection_popup(popup):
    def content(self):
        pass


def remove(ID=None, recrucive=False):
    if not ID: return
    i = 0
    while i < len(objects):
        if objects[i].ID == ID:
            del objects[i]
            if not recrucive: return
        else: i += 1