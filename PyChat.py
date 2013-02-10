# -*- coding: utf-8 -*-
# 12.12.2012


## TODO разобраться с относительностью путей к смайлам после преобразования py2exe 
##      иное решение - настройка пути к файлам смайлов в самом чате


from PyQt4 import QtGui,  QtCore
import sys
import time
import PyChatAPI.defaultmsgprocessor
import PyChatAPI.connector
import PyChatAPI.controller
import PyChatGUI.pychatgui

class PyChat(object):

    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.gui = PyChatGUI.pychatgui.PyChatGui()
        self.main_logic = MainLogic()
        self.gui.connect(self.main_logic, QtCore.SIGNAL('setText(QString)'), self.gui.setText)
        self.gui.show()
        self.main_logic.start()  
        sys.exit(app.exec_())
        
class MainLogic(QtCore.QThread):
    
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.controller = PyChatAPI.controller.Controller()
        # self.connector = PyChatAPI.connector.Connector()
        # self.controller.register_observer('CONNECTOR', self.connector)
        # self.connector.register_observer(self.controller)
        
        #self.connect(self, QtCore.SIGNAL('getStringFromInputLine(QString)'), self.getStringFromInputLine)
            
    def run(self):
        self.abc = 'test_1'
        main_loop = True
        while main_loop:
            #print 'q'

            self.emit(QtCore.SIGNAL('setText(QString)'),self.abc)
            time.sleep(1)

        
if __name__ == '__main__':
    PyChat()
