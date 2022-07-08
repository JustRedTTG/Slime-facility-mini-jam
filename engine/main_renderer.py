import pygame as pg
import engine.window as window
import engine.object_renderer as object_renderer

def handle_render():
    window.dis.fill((0,0,0))
    halt = False

    for object in object_renderer.objects:
        object.render()
        halt = halt and object.halt