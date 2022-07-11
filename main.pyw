import os
import engine
import engine.action, engine.object_renderer, engine.main_renderer
import threading

engine.data.pre_init()
engine.create_window()
if engine.data.debug and os.path.exists('save.dat'): os.remove('save.dat')
engine.game.load()

threading.Thread(target=engine.data.init).start()
engine.add_action(engine.action.loading_popup(
    hint='Please wait...',
    ID='main: data.init'))

while not engine.data.is_init:
    engine.prepare_events()
    engine.window_events(False)

    engine.handle_render()
    engine.handle_actions()

    engine.flip()
engine.add_action(engine.action.close_popup('main: data.init'))
engine.main_renderer.current_screen = 0
while engine.data.run:
    engine.prepare_events()
    engine.window_events()
    engine.input_events()

    engine.handle_render()
    engine.handle_level()

    engine.handle_actions()

    engine.flip()