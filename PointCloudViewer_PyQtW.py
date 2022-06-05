from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import numpy as np
import math
import pye57
import threading

class PointCloudViewer_PyQtW(QWidget):
    def __init__(self,parent = None,pointsPerThread = 4000,threadsNum = 4,red = 0,green = 255,blue = 0,backgroundColor = "grey"):
        super().__init__()
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setMouseTracking(True)
        self.xW = 0
        self.yW = 0
        #mouse left pressed
        self.mLP = False
        #mouse left pressed position X
        self.mLPPosX = 0
        #mouse left pressed position Y
        self.mLPPosY = 0
        #mouse middle pressed
        self.mMP = False
        #mouse middle pressed position X
        self.mMPPoX = 0
        #mouse middle pressed position Y
        self.mMPosY = 0
        #zoof factor
        self.zF = 2048.0
        #mouse last position X
        self.mLPX = 0.0
        #mouse last position Y
        self.mLPY = 0.0
        self.pointsPerThread = pointsPerThread
        self.threadsNum = threadsNum
        self.red = red
        self.green = green
        self.blue = blue
        self.SetBackgroundColor("grey")
        self.pointCloudLst = []
        self.projectionMatrixLst = []
        for i in range(threadsNum):
            self.projectionMatrixLst.append("")

    def SetBackgroundColor(self,backgroundColor):
        s = "background-color:" + backgroundColor + ";"
        self.setStyleSheet(s)

    def Resize(self,width,height):
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

    def mousePressEvent(self,event):
        pos = event.pos()
        if event.buttons() == QtCore.Qt.LeftButton:
            self.mLP = True
            self.mLPPosX = pos.x()
            self.mLPPosY = pos.y()
        elif event.buttons() == QtCore.Qt.MidButton:
            self.mMP = True
            self.mMPPosX = pos.x()
            self.mMPPosY = pos.y()

    def mouseReleaseEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.mLP = False
        elif event.button() == Qt.MidButton:
            self.mMP = False

    def wheelEvent(self,QMouseEvent):
        delta = QMouseEvent.angleDelta()
        if delta.y() > 0:
            self.zF = self.zF * 2.0
            self.xW = self.xW + (1.0/self.zF)*self.mLPX
            self.yW = self.yW + (1.0/self.zF)*self.mLPY
        else:
            self.zF = self.zF / 2.0
            self.xW = self.xW - (0.5/self.zF)*self.mLPX
            self.yW = self.yW - (0.5/self.zF)*self.mLPY
        self.update()

    def mouseMoveEvent(self,QMouseEvent):
        pos = QMouseEvent.pos()
        self.mLPX = pos.x()
        self.mLPY = pos.y()
        if self.mMP:
            dx = (pos.x() - self.mMPPosX)
            dy = (pos.y() - self.mMPPosY)
            self.xW = self.xW - dx/self.zF
            self.yW = self.yW - dy/self.zF
            self.mMPPosX = pos.x()
            self.mMPPosY = pos.y()
        else:
            if self.mLP:
                dPhi = ((pos.x() - self.mLPPosX)/self.width())*2*math.pi
                dTheta = ((pos.y() - self.mLPPosY)/self.height())*2*math.pi
                self.Rotate(-dTheta,dPhi)
                self.mLPPosX = pos.x()
                self.mLPPosY = pos.y()
        self.update()

    def ImportPointCloud(self,pointCloudXYZ):
        m = pointCloudXYZ
        n = min(self.pointsPerThread*self.threadsNum,m.shape[1])
        r = np.zeros(m.shape[1],dtype = "bool")
        r[0:n] = 1
        np.random.shuffle(r)
        m = m[:,r]
        #Calculate centroid and move Point Cloud
        t = np.sum(m,axis = 1)
        t = t / m.shape[1]
        centroid = np.zeros((3,1))
        centroid[0][0] = t[0]
        centroid[1][0] = t[1]
        centroid[2][0] = t[2]
        t = m - centroid
        self.pointCloudLst = []
        m = int(n/self.threadsNum)
        for i in range(self.threadsNum):
            pointCloud = t[:,i*m:min((i+1)*m,t.shape[1])]
            self.pointCloudLst.append(pointCloud)
        self.update()

    def ImportE57(self,e57):
        e57 = pye57.E57(e57)
        data = e57.read_scan(0)
        assert isinstance(data["cartesianX"], np.ndarray)
        assert isinstance(data["cartesianY"], np.ndarray)
        assert isinstance(data["cartesianZ"], np.ndarray)
        x = data["cartesianX"]
        y = data["cartesianY"]
        z = data["cartesianZ"]
        pointsNum = x.shape[0]
        pointCloudXYZ= np.zeros((3,pointsNum))
        pointCloudXYZ[0,:] = x
        pointCloudXYZ[1,:] = y
        pointCloudXYZ[2,:] = z
        self.ImportPointCloud(pointCloudXYZ)

    def ThreadRotate(self,threadId,dPhi,dTheta):
        pointCloudXYZ = self.pointCloudLst[threadId]

        r1 = np.zeros((3,3))
        r1[0][0] = 1
        r1[1][1] = math.cos(dPhi)
        r1[1][2] = -math.sin(dPhi)
        r1[2][1] = math.sin(dPhi)
        r1[2][2] = math.cos(dPhi)

        r2 = np.zeros((3,3))
        r2[0][0] = math.cos(dTheta)
        r2[0][2] = math.sin(dTheta)
        r2[1][1] = 1
        r2[2][0] = -math.sin(dTheta)
        r2[2][2] = math.cos(dTheta)

        r = np.matmul(r1,r2)
        pointCloudXYZ = np.matmul(r,pointCloudXYZ)
        self.pointCloudLst[threadId] = pointCloudXYZ

    def Rotate(self,dPhi,dTheta):
        if self.pointCloudLst:
            threads = []
            for i in range(self.threadsNum):
                thrd = threading.Thread(target = self.ThreadRotate,args=(i,dPhi,dTheta),daemon = True)
                thrd.start()
                threads.append(thrd)
            for i in range(self.threadsNum):
                thrd = threads[i]
                thrd.join()
        self.update()

    def ThreadGenerateProjectionMatrix(self,threadId):
        t = self.pointCloudLst[threadId]
        tProjectionMatrix = np.zeros((2,t.shape[1]))
        x = t[0,:]
        y = t[1,:]
        x = self.zF*(x - self.xW)
        y = self.zF*(y - self.yW)
        tProjectionMatrix[0,:] = x
        tProjectionMatrix[1,:] = y
        self.projectionMatrixLst[threadId] = tProjectionMatrix

    def GenerateProjectionMatrix(self):
        threads = []
        for i in range(self.threadsNum):
            thrd = threading.Thread(target = self.ThreadGenerateProjectionMatrix,args=(i,),daemon = True)
            thrd.start()
            threads.append(thrd)
        for i in range(self.threadsNum):
            thrd = threads[i]
            thrd.join()

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        if len(self.pointCloudLst) != 0:
            self.GenerateProjectionMatrix()
            painter.setPen((QPen(QColor(self.red,self.green,self.blue),2,Qt.SolidLine)))
            for i in range(len(self.projectionMatrixLst)):
                projectionMatrix = self.projectionMatrixLst[i]
                for j in range(projectionMatrix.shape[1]):
                    x = projectionMatrix[0][j]
                    y = projectionMatrix[1][j]
                    painter.drawPoint(int(x),int(y))
        painter.end()


