class MenuBar:
    def __init__(self,parent):
        self.parent=parent
        parent.action_Exit.triggered.connect(parent.close)
