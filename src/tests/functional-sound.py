import math
import pyaudio

import sys
import matplotlib.pyplot as plt
import numpy as np
import PyQt5
import pyqtgraph as pg
import pyqtgraph.exporters

import time
from datetime import datetime, timedelta
from threading import Thread

# Pyqtgraph stuff


PyAudio = pyaudio.PyAudio
BITRATE = 11050     #frames per second/frameset.
LENGTH = 15     #in seconds
NUMBER_OF_FRAMES = int(BITRATE * LENGTH)
REST_FRAMES = NUMBER_OF_FRAMES % BITRATE
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 512
PIXEL_SIZE = 2

def test_function(t):
    return (t*((t>>12|t>>8)&63&t>>4)) % 256

def play_audio(sound_bytes):
    p = PyAudio()
    #p = pyaudio.PyAudio
    stream = p.open(format = p.get_format_from_width(1),
                    channels = 1,
                    rate = BITRATE,
                    output = True)
    time.sleep(1)
    stream.write(sound_bytes)
    stream.stop_stream()
    stream.close()
    p.terminate()
'''
def show_graphics(values):
    # Setting up
    TITLE = "Audio"
    y = np.array(values)
    x = range(0, 1000)
    print(len(values))
    plt = pg.plot(x, y[0:1000], title=TITLE, pen='r')
    plt.showGrid(x=True, y=True)
'''
#'''
class Graphics(object):
    def __init__(self):
        self.b = 0
        self.min = 0
        self.max = 300
        self.num_values = 300
        self.app = pg.QtGui.QApplication(sys.argv)
        self.values = None

    def animate_graphics(self, values):
        self.values = values
        print(len(values))
        timer = pg.QtCore.QTimer()
        timer.timeout.connect(self.update_graphics)
        timer.start(10)
        self.start_graphics()

    def update_graphics(self):
        x = np.arange(0, 3.0, 0.01)
        y = self.values[self.min:self.max]
        self.min = self.max
        self.max = self.max + self.num_values
        self.b += 0.1
        self.show_graphics(x,y)

    def show_graphics(self, x, y):
        TITLE = "Audio"
        plt = pg.plot(x, y, title=TITLE, pen = 'r')
        plt.showGrid(x=True, y=True)

    def start_graphics(self):
        # Start graphing
        if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
            pg.QtGui.QApplication.exec_()

#'''
'''
def start_graphics():
    # Start graphing
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
'''

def main():

    # Generate values
    values = []
    print("\nGenerating values...")
    for x in range(NUMBER_OF_FRAMES + REST_FRAMES):
        if(x%1000==0):
            print('*',end='')
        values.append(test_function(x))
    print()
    print(values)

    # Generate wave data
    wave_data = []
    print("\nGenerating audio...")
    for i in range(len(values)):
        if(i%1000==0):
            print('*',end='')
        wave_data.append(chr(values[i]))
    sound_bytes = ''.join(wave_data)

    # Start audio
    print("Playing audio...")
    t = Thread(target=play_audio, args=(sound_bytes,))
    t.start()


    # Show graphics
    print("Showing graphics...")
    #'''
    g = Graphics()
    g.animate_graphics(values)
    #'''
    #show_graphics(values)
    #start_graphics()

main()
