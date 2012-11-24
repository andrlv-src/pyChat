# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import PyChatAPI.defaultlistener
import PyChatGUI.pychatgui

class Main(object):
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.gui = PyChatGUI.pychatgui.PyChatGui()
        #self.listener = PyChatAPI.defaultlistener.DefaultListener()
        self.gui.show()
        sys.exit(app.exec_())




if __name__ == '__main__':
    Main()
        
