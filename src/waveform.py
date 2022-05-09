from PySide2.QtCore import Signal
import pyqtgraph as pg


class Waveform(pg.PlotItem):
    data_available = Signal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_available.connect(self.update)
        self.trace = self.plot(pen='g')
        self.disableAutoRange()
        self.setXRange(0, 1024, padding=0)
        self.setYRange(0, 256, padding=0)

    def update(self, data: list) -> None:
        self.trace.setData(data)
