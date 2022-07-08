import engine
import engine.action, engine.object_renderer
import threading

engine.create_window()
engine.game.load()

threading.Thread(target=engine.data.init).start()
engine.object_renderer.objects.append(engine.object_renderer.loading_popup(engine.action.loading_popup(
    hint='Please wait...',
    ID='main: data.init')))

while not engine.data.is_init:
    engine.prepare_events()

    engine.handle_render()
    engine.handle_actions()

    engine.flip()
engine.object_renderer.remove('main: data.init')
while True:
    engine.prepare_events()
    engine.window_events()

    engine.handle_render()
    engine.handle_actions()

    engine.flip()