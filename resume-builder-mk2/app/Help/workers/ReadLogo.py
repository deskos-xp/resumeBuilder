from PyQt5.QtCore import QObject,QThreadPool,QThread,QRunnable,pyqtSignal,pyqtSlot
from PyQt5.QtGui import QImage,QPixmap
import os,sys
from io import BytesIO

class ReadLogoSignals(QObject):
    killMe:bool=False
    finished:pyqtSignal=pyqtSignal()
    hasError:pyqtSignal=pyqtSignal(Exception)
    hasQPixmap:pyqtSignal=pyqtSignal(QPixmap)
    hasQImage:pyqtSignal=pyqtSignal(QImage)
    hasBytesIO:BytesIO=pyqtSignal(BytesIO)

    @pyqtSlot()
    def kill(self):
        self.killMe=True

class ReadLogo(QRunnable):
    def __init__(self,path):
        super(ReadLogo,self).__init__()
        self.path=path
        self.signals=ReadLogoSignals()

    def run(self):
        try:
            bio:BytesIO=BytesIO()
            with open(os.path.abspath(self.path),"rb") as fd:
                while True:
                    d=fd.read(1024)
                    if not d:
                        break
                    bio.write(d)
            bio.seek(0)
            self.signals.hasBytesIO.emit(bio)
            img=QImage.fromData(bio.read())
            self.signals.hasQImage.emit(img)
            pixmap=QPixmap.fromImage(img)
            self.signals.hasQPixmap.emit(pixmap)

        except Exception as e:
            self.signals.hasError.emit(e)
        self.signals.finished.emit()
