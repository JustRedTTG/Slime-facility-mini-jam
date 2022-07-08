import pygame as pg
import engine.data as data
pg.init()

def create_window():
    pg.display.set_mode(data.screenSize, pg.RESIZABLE)
    pg.display.set_caption(f'{data.title} ver. {data.version}')
    pg.display.set_icon(data.icon)