import engine

engine.create_window()

while True:
    engine.prepare_events()
    engine.window_events()

    engine.handle_render()
    engine.handle_actions()

    engine.flip()