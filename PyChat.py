# -*- coding: utf-8 -*-

from PyQt4 import QtGui,  QtCore
import sys
import PyChatAPI.defaultlistener
import PyChatGUI.pychatgui
import PyChatAPI.defaultsender

class PyChat(object):
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.gui = PyChatGUI.pychatgui.PyChatGui()
        #self.listener = PyChatAPI.defaultlistener.DefaultListener()
        self.gui.show()
        sys.exit(app.exec_())
        
class MainLogic(QtCore.QThread):
    # конструктор
    # выполняем конструктор предка
    # создаем объекты листенер и сендер 
    
    
    # переопределяем метод run()
        # 
    pass

if __name__ == '__main__':
    PyChat()
        
