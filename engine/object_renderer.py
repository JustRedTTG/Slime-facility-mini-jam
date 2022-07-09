import math
import pygame as pg
import engine.window as window
import engine.data as data
import engine.eventhandler as eventhandler

objects = []
def fontScaler(x, text, sides=10):
    factor = len(text) - 10
    scale = factor * .0033
    scale = factor * scale * .026
    scale = (800 * .1 - len(text) * scale) / (800 + x + sides)
    return int(window.size[0] * scale)

def boxart(migrade,ex,ey, border_factor=1, curve_factor=1, color=data.boxart_color):
    i = 0
    size = (ex-migrade[0], ey-migrade[1])
    borderlength = int((size[0] + size[1]) * .0075 * border_factor)
    for y in range(migrade[1] + borderlength, ey - borderlength):
        pg.draw.line(window.dis, data.boxart_pallet[i],
                     (migrade[0]+borderlength, y),
                     (ex - borderlength, y))
        i += 1
        if i >= len(data.boxart_pallet): i = 0
    pg.draw.rect(window.dis, color,
                 (*migrade, ex - migrade[0], ey - migrade[1]),
                 borderlength,int(size[0] * borderlength * 0.005 * curve_factor))

# OBJECTS

class object:
    action = None
    halt = False
class popup(object):
    def __init__(self, action):
        self.action = action
        self.halt = True
        self.ID = action.ID
        self.buildSize = tuple(window.size)
        self.font()
    def font(self):
        scale = fontScaler(window.size[0], self.action.title, -200)
        self.title = pg.font.Font('font.ttf', scale).render(self.action.title,True, data.box_text_color)
    def content(self): pass
    def sizeRefresh(self): pass
    def render(self):
        if self.buildSize != window.size:
            self.buildSize = tuple(window.size)
            self.font()
            self.sizeRefresh()
        migrade = int(window.size[0] * .1), int(window.size[1] * .1)
        boxart(migrade, window.size[0] - migrade[0], window.size[1] - migrade[1])
        window.dis.blit(self.title, (window.size[0] * .5 - self.title.get_width() * .5, migrade[1]*2))
        self.content()

class loading_popup(popup):
    rotation = 0
    speed = 2
    icon = None
    def makeIcon(self):
        size = (int(0.04  * window.size[0] * 2), int(0.04 * window.size[0] * 2))
        self.icon = pg.transform.scale(data.loading_icon, size)
    def sizeRefresh(self): self.makeIcon()
    def content(self):
        if not self.icon: self.makeIcon()
        canvas = pg.transform.rotate(self.icon, self.rotation)
        self.rotation -= self.speed

        window.dis.blit(canvas, (
            window.size[0] * .5 - canvas.get_width() * .5,
            window.size[1] * .75 - canvas.get_height() * .5
        ))
class selection_popup(popup):
    button_width = 1
    option1, option2 = None, None
    lock = False
    def font2(self):
        scale = fontScaler(self.button_width, self.action.option1, self.button_width)
        self.option1 = pg.font.Font('font.ttf', scale).render(self.action.option1, True, data.box_text_color)
        scale = fontScaler(self.button_width, self.action.option2, self.button_width)
        self.option2 = pg.font.Font('font.ttf', scale).render(self.action.option2, True, data.box_text_color)
    def sizeRefresh(self): self.font2()
    def content(self):
        migrade = int(window.size[0] * .2), int(window.size[1] * .3) # The migrade

        # Rects of buttons
        rect1 = pg.Rect(migrade[0], window.size[1] - migrade[1], window.size[0] * .5 - migrade[0] * .25, int(window.size[1] * .85))
        rect2 = pg.Rect(window.size[0] * 0.5 + migrade[0] * .25, window.size[1] - migrade[1], window.size[0] - migrade[0], int(window.size[1] * .85))
        self.button_width = rect1.w-rect1.x
        if not self.option1 or not self.option2: self.font2()
        mouse_rect = pg.Rect(*eventhandler.mouse_position, 1, 1) # Mouse rect

        # Check collision
        if mouse_rect.colliderect(pg.Rect(rect1.x, rect1.y, rect1.w-rect1.x, rect1.h-rect1.y)):
            color1 = data.boxart_color_collide
            if not self.lock and eventhandler.mouse_left:
                self.lock = True
                for act in self.action.action1:
                    eventhandler.action_pool.append(act)
        else: color1 = data.boxart_color
        if mouse_rect.colliderect(pg.Rect(rect2.x, rect2.y, rect2.w-rect2.x, rect2.h-rect2.y)):
            color2 = data.boxart_color_collide
            if not self.lock and eventhandler.mouse_left:
                self.lock = True
                for act in self.action.action2:
                    eventhandler.action_pool.append(act)
        else: color2 = data.boxart_color

        # Draw BoxArt
        if self.lock: return
        boxart((rect1.x, rect1.y), rect1.w, rect1.h, color=color1)
        window.dis.blit(self.option1, (rect1.w - (rect1.w - rect1.x) * .5 - self.option1.get_width() * .5, rect1.h - (rect1.h - rect1.y) * .5 - self.option1.get_height() * .5))
        boxart((rect2.x, rect2.y), rect2.w, rect2.h, color=color2)
        window.dis.blit(self.option2, (rect2.w - (rect2.w - rect2.x) * .5 - self.option2.get_width() * .5, rect2.h - (rect2.h - rect2.y) * .5 - self.option2.get_height() * .5))


def remove(ID=None, recursive=False):
    if not ID: return
    i = 0
    while i < len(objects):
        if objects[i].ID == ID:
            del objects[i]
            if not recursive: return
        else: i += 1