import os.path
import engine.save as manager

class level_data:
    def __init__(self, coins):
        self.coins_collected = coins

class game_data:
    def __init__(self):
        self.unlocked_level = 0
        self.complete_levels = set()
slot = game_data()
def save():
    global slot
    manager.save('save.dat', slot)

def load():
    global slot
    if os.path.exists('save.dat'): slot = manager.load('save.dat')[0]