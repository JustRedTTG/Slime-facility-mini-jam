import engine.data as data
save = 0
close_popup = 1
quit = 2

class selection_popup:
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

class loading_popup:
    def __init__(self,
        title = 'Loading...',
        hint = 'Someone forgot to change the hint here lmao',
        ID = None):

        self.title = title
        self.hint = hint
        self.textcolor = data.box_text_color
        self.ID = ID