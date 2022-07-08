import engine.eventhandler as eventhandler
import engine.action as a
import engine.object_renderer as renderer

def handle_actions():
    i = 0
    while i < len(eventhandler.action_pool):
        if type(eventhandler.action_pool[i]) == a.selection_popup: # Selection popup?
            renderer.objects.append(renderer.selection_popup(eventhandler.action_pool[0])) # append a selection popup object
        del eventhandler.action_pool[0] # clear the action from the pool