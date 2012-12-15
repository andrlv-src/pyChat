# -*- coding: utf-8 -*-
# 12.12.2012


## TODO разобраться с относительностью путей к смайлам после преобразования py2exe 
##      иное решение - настройка пути к файлам смайлов в самом чате

## TODO обязательно проверять входные строки ко всем методам обработчиков входящих строк

from PyQt4 import QtGui,  QtCore
import sys
import PyChatAPI.defaultmsgprocessor
import PyChatAPI.connector
import PyChatGUI.pychatgui

class PyChat(object):

    xx = ''
    
    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        self.gui = PyChatGUI.pychatgui.PyChatGui()
        self.ml = MainLogic()
        self.gui.connect(self.ml, QtCore.SIGNAL('setText(QString)'), self.gui.setText)
        self.gui.show()
        self.ml.start()  
        sys.exit(app.exec_())
        
class MainLogic(QtCore.QThread):
    
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.connector = PyChatAPI.connector.Connector()

        
        self.msg_processor = PyChatAPI.defaultmsgprocessor.DefaultMsgProcessor()
        # self.controller = PyChatAPI.controller.Connector()
        # self.controller.connect(self, QtCore.SIGNAL('getText(QString)'), self.getText())
            
    def run(self):
        
        while True:
            self.xx = self.connector.receive()

            # print '[debug]' + self.xx
            self.xx = self.msg_processor.process_message(self.xx)
            # <- controller
            self.xx = self.xx.get_string()
            self.emit(QtCore.SIGNAL('setText(QString)'),self.xx)

            # listen GUI
            # process message
        
if __name__ == '__main__':
    PyChat()
