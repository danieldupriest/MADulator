from PySide2 import QtCore, QtWidgets
from madulator import Madulator

app = QtWidgets.QApplication([])
mad = Madulator()

# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
