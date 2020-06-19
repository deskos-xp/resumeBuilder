import os,sys,json
from PyQt5.QtCore import QObject,QThreadPool,QRunnable,QThread
from PyQt5.QtWidgets import QFileDialog
class Json:
    def __init__(self,parent):
        self.parent=parent
        self.data=dict()
        
        parent.navigate_json.clicked.connect(self.getFname)
        #parent.json_path

    def saveJson(self,js):
        delKeys=[]
        for i in js.keys():
            if js.get(i) == []:
                delKeys.append(i)
        for i in delKeys:
            js.__delitem__(i)

        with open(self.parent.json_path.text(),"w") as fd:
            json.dump(dict(js),fd)

    def setData(self,data):
        self.data=data
        if self.parent.json_path.text() != "":
            self.saveJson(data)
        else:
            print(json.dumps(self.data))

    def getFname(self,state):
        self.fname=QFileDialog.getSaveFileName(self.parent,"Save Data as JSON",'','json (*.json) ;; JSON(*.JSON);;All Files(*)',options=QFileDialog.DontUseNativeDialog)
        self.parent.json_path.setText(self.fname[0])
