import numpy as np
import math

class PointCloudGenerator():
    def __init__(self,shape,parList):
        self.shape = shape
        self.parList = parList
        self.GeneratePointCloud()

    def GetPointCloud(self):
        return self.pointCloud

    def GeneratePointCloud(self):
        if self.shape == "sphere":
            x0 = self.parList[0]
            y0 = self.parList[1]
            z0 = self.parList[2]
            r = self.parList[3]
            n1 = 50
            n2 = 50
            self.pointCloud = np.zeros((3,n1*n2))
            phi = np.linspace(0,2*math.pi,n1)
            dTheta = 2*math.pi / n2
            theta = 0
            for i in range(n2-1):
                x = x0 + r*math.cos(theta)*np.cos(phi)
                y = y0 + r*math.sin(theta)*np.cos(phi)
                z = z0 + r*np.sin(phi)
                theta = theta + dTheta
                self.pointCloud[0,i*n1:(i+1)*n1] = x
                self.pointCloud[1,i*n1:(i+1)*n1] = y
                self.pointCloud[2,i*n1:(i+1)*n1] = z
