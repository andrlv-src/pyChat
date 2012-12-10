# -*- coding: utf-8 -*-



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
        self.gui.connect(self.ml, QtCore.SIGNAL('setChatLog(QString)'), self.gui.setChatLog)
        self.ml.start()  
        self.gui.show()
        sys.exit(app.exec_())
        
class MainLogic(QtCore.QThread):
    
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.connector = PyChatAPI.connector.Connector()
        self.msg_processor = PyChatAPI.defaultmsgprocessor.DefaultMsgProcessor()
            
    def run(self):
        
        while True:
            self.xx = self.connector.reciever()

            # print '[debug]' + self.xx
            self.xx = self.msg_processor.process_message_from_server(self.xx)
            self.xx = self.xx.get_string()
            self.emit(QtCore.SIGNAL('setChatLog(QString)'),self.xx)

            # listen GUI
            # process message
        
if __name__ == '__main__':
    PyChat()
