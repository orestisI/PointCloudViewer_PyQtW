from PointCloudViewer_PyQtW import *
import sys
import math
import time
import numpy as np

class PointCloudViewer_PyQtW_Ex(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        super(PointCloudViewer_PyQtW_Ex,self).__init__(*args,**kwargs)
        self.pointCloudViewer_PyQtW = PointCloudViewer_PyQtW()
        self.setCentralWidget(self.pointCloudViewer_PyQtW)

    '''
    def GenerateSphere(self):
        sphere = PointCloudGenerator("sphere",[0,0,0,100])
        pointCloudXYZ = sphere.GetPointCloud()
        pointsNum = pointCloudXYZ.shape[1]
        r = np.random.randint(256,pointsNum)
        g = np.random.randint(256,pointsNum)
        b = np.random.randint(256,pointsNum)
        rgb = np.zeros((3,pointsNum))
        rgb[0,:] = r
        rgb[1,:] = g
        rgb[2,:] = b
        self.pointCloudViewer.AddPointCloud([pointCloudXYZ,rgb])

    '''
    '''
    def Bunny(self):
        e57 = "bunnyFloat.e57"

        e57 = pye57.E57("bunnyFloat.e57")

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
        print(pointCloudXYZ)
        r = np.random.randint(256,pointsNum)
        g = np.random.randint(256,pointsNum)
        b = np.random.randint(256,pointsNum)
        rgb = np.zeros((3,pointsNum))
        rgb[0,:] = r
        rgb[1,:] = g
        rgb[2,:] = b
        self.pointCloudViewer.AddPointCloud([pointCloudXYZ,rgb])

    '''

app = QtWidgets.QApplication(sys.argv)
t = PointCloudViewer_PyQtW_Ex(None)
t.show()
sys.exit(app.exec_())
