import engine.data as data
save = 0
quit = 1
class action:
    ID = None

class selection_popup(action):
    def __init__(self,
        title = 'Please choose',
        option1 = 'Yes', action1 = None,
        option2 = 'No' , action2 = None,
        ID = None):

        self.title = title
        self.option1 = option1
        self.action1 = action1

        self.option2 = option2
        self.action2 = action2

        self.ID = ID

class loading_popup(action):
    def __init__(self,
        title = 'Loading...',
        hint = 'Someone forgot to change the hint here lmao',
        ID = None):

        self.title = title
        self.hint = hint
        self.textcolor = data.box_text_color
        self.ID = ID

class close_popup(action):
    def __init__(self, ID): self.ID = ID

class remove_object(action):
    def __init__(self, target, recursive=False, ID=None):
        self.target = target,
        self.recursive = recursive
        self.ID = ID
class remove_custom_object(remove_object): pass