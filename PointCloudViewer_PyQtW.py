from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QPoint,QRect
import numpy as np
import math
import pye57
from PointCloudViewer_Viewer_PyQtW import *
from PointCloudViewer_Dlg_PyQtW import *

class PointCloudViewer_PyQtW(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.parent = parent

        self.mainLayout = QHBoxLayout()

        self.pointCloudViewer_Dlg_PyQtW = PointCloudViewer_Dlg_PyQtW(self)
        self.pointCloudViewer_Dlg_PyQtW.setFixedWidth(self.width()/8)
        self.pointCloudViewer_Viewer_PyQtW = PointCloudViewer_Viewer_PyQtW(self)

        self.mainLayout.addWidget(self.pointCloudViewer_Dlg_PyQtW)
        self.mainLayout.addWidget(self.pointCloudViewer_Viewer_PyQtW)

        self.setLayout(self.mainLayout)

    def resizeEvent(self,event):
        self.pointCloudViewer_Dlg_PyQtW.setFixedWidth(self.width()/8)

