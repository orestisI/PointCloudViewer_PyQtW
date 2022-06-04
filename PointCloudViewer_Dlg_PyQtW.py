from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QPoint,QRect

class PointCloudViewer_Dlg_PyQtW(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.parent = parent

        self.mainLayout = QVBoxLayout()

        self.liveStreamModeW = QWidget()
        self.liveStreamModeLayout = QHBoxLayout()
        self.liveStreamModeLabel = QLabel("Live Stream Mode")
        self.liveStreamModeCheckBox = QCheckBox()
        self.liveStreamModeLayout.addWidget(self.liveStreamModeLabel)
        self.liveStreamModeLayout.addWidget(self.liveStreamModeCheckBox)
        self.liveStreamModeW.setLayout(self.liveStreamModeLayout)
        self.mainLayout.addWidget(self.liveStreamModeW)

        self.setLayout(self.mainLayout)

