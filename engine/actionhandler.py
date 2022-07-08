import engine.eventhandler as eventhandler
import engine.action as a
import engine.object_renderer as renderer
import engine.game as slot_manager

def handle_actions():
    i = 0
    while i < len(eventhandler.action_pool):
        if type(eventhandler.action_pool[i]) == a.selection_popup: # Selection popup?
            renderer.objects.append(renderer.selection_popup(eventhandler.action_pool[0])) # append a selection popup object
        elif type(eventhandler.action_pool[i]) == a.loading_popup: # Loading popup?
            renderer.objects.append(renderer.loading_popup(eventhandler.action_pool[0])) # append a loading popup object
        elif type(eventhandler.action_pool[i]) == a.close_popup:
            renderer.remove(eventhandler.action_pool[i].ID)
        elif eventhandler.action_pool[i] == a.save:
            slot_manager.save()
        elif eventhandler.action_pool[i] == a.quit:
            exit()
        else:
            print(eventhandler.action_pool[i])
        del eventhandler.action_pool[0] # clear the action from the pool