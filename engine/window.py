import pygame as pg
import engine.data as data
pg.init()
flip = pg.display.flip
dis = pg.Surface # Syntax highlighting
size = data.screenSize

def create_window():
    global dis
    pg.display.set_mode(data.screenSize, pg.HIDDEN)
    pg.display.set_caption(f'{data.title} ver. {data.version}')
    pg.display.set_icon(data.icon)
    dis = pg.display.set_mode(data.screenSize, pg.RESIZABLE)

