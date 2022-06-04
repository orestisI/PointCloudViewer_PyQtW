from PointCloudViewer_PyQtW import *
import sys
import math
import time
import numpy as np

class PointCloudViewer_PyQtW_Ex(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(PointCloudViewer_PyQtW_Ex,self).__init__(*args,**kwargs)
        self.pointCloudViewer_PyQtW = PointCloudViewer_PyQtW()
        self.pointCloudViewer_PyQtW.ImportE57("./e57Examples/bunnyFloat.e57")
        self.setCentralWidget(self.pointCloudViewer_PyQtW)


app = QtWidgets.QApplication(sys.argv)
t = PointCloudViewer_PyQtW_Ex(None)
t.show()
sys.exit(app.exec_())
