import pygame as pg
import engine.data as data
import engine.action as action
import engine.window as window_handler
import engine.object_renderer as object_renderer

events = [pg.event.Event] # Syntax highlighting
action_pool = []

assigned_key_actions = {}

def add_action(act:action.action):
    global action_pool
    action_pool.append(act)
#
mouse_position = (0, 0)
mouse_left, mouse_middle, mouse_right = False, False, False
#
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

def window_events(enable_quitting=True):
    global events
    for event in events:
        if event.type == pg.QUIT and enable_quitting:
            if not (check_action_pool('eventhandler: save and quit') or check_object_pool('eventhandler: save and quit')):
                action_pool.append(action.selection_popup('Save and quit?',
                                                          'Quit' , [action.close_popup('eventhandler: save and quit'), action.save, action.quit],
                                                          'Cancel', [action.close_popup('eventhandler: save and quit')],
                                                          'eventhandler: save and quit'))
        elif event.type == pg.WINDOWRESIZED: window_handler.size = window_handler.dis.get_size()
def input_handle_key(event:pg.event.Event, key1, key2, neutral, v1, v2, value):
    if event.type == pg.KEYDOWN and event.key == key1: return v1
    elif event.type == pg.KEYDOWN and event.key == key2: return v2
    elif event.type == pg.KEYUP and (event.key == key1 or event.key == key2): return neutral
    return value

def input_handle_pressed(event:pg.event.Event, key1, up, down, value):
    if event.type == pg.KEYDOWN and event.key == key1: return down
    elif event.type == pg.KEYUP and event.key == key1: return up
    return value

def input_events(halt=False):
    global events, mouse_position, mouse_left, mouse_middle, mouse_right
    for event in events:
        if event.type == pg.MOUSEMOTION: mouse_position = event.pos
        elif event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP: mouse_left, mouse_middle, mouse_right = pg.mouse.get_pressed()
        if data.movement_target == 'any':
            data.force[0] = input_handle_key(event, data.keys['left'], data.keys['right'], 0, -1, 1, data.force[0])
            data.force[1] = input_handle_key(event, data.keys['up'], data.keys['down'], 0, -1, 1, data.force[1])
        elif data.movement_target == 'player' and data.force[0]+data.force[0] == 0:
            data.force[0] = input_handle_key(event, data.keys['left'], data.keys['right'], data.force[0], -1, 1, data.force[0])
            data.force[1] = input_handle_key(event, data.keys['up'], data.keys['down'], data.force[1], -1, 1, data.force[1])
        data.enter = input_handle_pressed(event, data.keys['space'], False, True, data.enter)
        data.enter = input_handle_pressed(event, data.keys['return'], False, True, data.enter)