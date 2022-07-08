import pygame as pg
import engine.data as data
import engine.action as action
import engine.window as window_hadler
import engine.object_renderer as object_renderer

events = [pg.event.Event] # Syntax highlighting

action_pool = []

def prepare_events():
    global events
    events = pg.event.get()

def check_action_pool(ID='eventhandler: null'):
    for action in action_pool:
        if action.ID == ID: return True
    return False
def check_object_pool(ID='eventhandler: null'):
    for object in object_renderer.objects:
        if object.ID == ID: return True
    return False

def window_events():
    global events
    for event in events:
        if event.type == pg.QUIT:
            if not (check_action_pool('eventhandler: save and quit') or check_object_pool('eventhandler: save and quit')):
                action_pool.append(action.selection_popup('Save and quit?',
                                                          'Quit.' , [action.close_popup, action.save, action.quit],
                                                          'Cancel', [action.close_popup],
                                                          'eventhandler: save and quit'))
        elif event.type == pg.WINDOWRESIZED: window_hadler.size = window_hadler.dis.get_size()
