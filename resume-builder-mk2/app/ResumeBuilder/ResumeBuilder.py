class ResumeBuilder:
    def __init__(self,parent):
        self.parent=parent
        self.data=None

    def load_data(self,data):
        self.data=data

    def gen(self):
        pass
