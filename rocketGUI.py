

from PyQt6 import QtCore, QtGui, QtWidgets, uic
from pyqtgraph import PlotWidget, plot
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import sys
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi('rocketGUI.ui', self)
        self.timer = QtCore.QElapsedTimer()
        #self.timer.setInterval(500)

    def real_time_plot(self):
        data = open('/Users/dharmikpatel/Downloads/launch_example.csv', 'r')
        data = data.readlines()[1:]
        data = [x.split(',') for x in data]
        self.timer.start()
        data_index = 0
        print(type(self.graphWidget))
        print(data)
        x_list = []
        y_list = []
        while True:
            if self.timer.elapsed() % 500 == 0:
                try:
                    x = float(data[data_index][0])
                    y = float(data[data_index][1])
                except:
                    break

                x_list.append(x)
                y_list.append(y)
                self.graphWidget.plot((x_list), (y_list))
                data_index += 1

                QtGui.QGuiApplication.processEvents()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    main.real_time_plot()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
