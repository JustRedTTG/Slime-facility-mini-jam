"""An Engine made entirely for slime facility"""
import pygame as pg
import engine.data as data
import engine.game as game
from engine.window import *
from engine.eventhandler import *
from engine.actionhandler import *
from engine.main_renderer import *
from engine.levelhandler import *

for i in range(data.middle_boxart.get_height()): data.boxart_pallet.append(data.middle_boxart.get_at((0, i)))