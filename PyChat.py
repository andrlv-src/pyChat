# -*- coding: utf-8 -*-



## TODO разобраться с относительностью путей к смайлам после преобразования py2exe 
##      иное решение - настройка пути к файлам смайлов в самом чате

from PyQt4 import QtGui,  QtCore
import sys
import PyChatAPI.defaultmsgprocessor
import PyChatAPI.connector
import PyChatGUI.pychatgui

class PyChat(object):
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.gui = PyChatGUI.pychatgui.PyChatGui()
        self.ml = MainLogic()
        self.ml.start()  
        self.gui.show()
        sys.exit(app.exec_())
        
class MainLogic(QtCore.QThread):
    
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.connector = PyChatAPI.connector.Connector()
            
    def run(self):
        
        while True:
            print self.connector.reciever()
            # process message
            # listen GUI
            # process message
        
if __name__ == '__main__':
    PyChat()
