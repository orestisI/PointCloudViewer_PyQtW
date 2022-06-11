# PointCloudViewer_PyQtW
Point Cloud Viewer Widget (Qt)
![Bunny](./Images/bunny.png)

##  Description
Python (Qt) Widget that can be used to view point clouds.

##  Install Dependencies

```bash
pip3 install PyQt5
pip3 install numpy
pip3 install pye57

```

##  Usage
```python
...
pointsPerThread = 4000 #Points that each thread will render->default = 4000
threadsNum = 4         #Number of threads that will render the image->default = 4
red = 0                #point cloud red value (0-255) -> default = 0
green = 255            #point cloud green value (0-255)-> default = 255
blue = 0               #point cloud blue value(0-255) -> default = 0

self.pointCloudViewer_PyQtW = PointCloudViewer_PyQtW(self,pointsPerThread,threadsNum,red,green,blue)
self.setCentralWidget(self.pointCloudViewer_PyQtW)
...

...
self.pointCloudViewer_PyQtW.ImportE57("path/to/e57/file")
...

```

## Example
```bash
python3 PointCloudViewer_PyQtW_Ex.py
```
