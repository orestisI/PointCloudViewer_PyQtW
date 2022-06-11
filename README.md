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
self.pointCloudViewer_PyQtW = PointCloudViewer_PyQtW()
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
