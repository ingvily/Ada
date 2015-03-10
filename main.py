#! /usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.getcwd() + "/GUI")
sys.path.append(os.getcwd() + "/Objects")
sys.path.append(os.getcwd() + "/robotImages")
sys.path.append(os.getcwd() + "/Robots")
from window import MainWindow
from PyQt4 import QtGui

f = open(os.devnull, 'w')
sys.stderr = f

if __name__ == "__main__":
   arena = sys.argv[1]
   app = QtGui.QApplication(sys.argv)
   app.setApplicationName("Python-Robocode")
   myapp = MainWindow(arena)
   myapp.show()
   sys.exit(app.exec_())

