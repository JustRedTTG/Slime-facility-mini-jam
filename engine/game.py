import os.path
import engine.save as manager
slot = None

class level_data:
    def __init__(self, coins):
        self.coins_collected = coins

class game_data:
    def __init__(self):
        self.unlocked_levels = [0]
        self.complete_levels = []

def save():
    global slot
    manager.save('save.dat', slot)

def load():
    global slot
    if os.path.exists('save.dat'): slot = manager.load('save.dat')[0]
    else:
        slot = game_data()
        save()