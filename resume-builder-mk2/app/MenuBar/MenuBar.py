from ..Help.Help import Help
class MenuBar:
    def getAbout(self):
        about=Help(self.parent)
    def __init__(self,parent):
        self.parent=parent
        parent.action_Exit.triggered.connect(parent.close)
        parent.actionAbout.triggered.connect(self.getAbout)


