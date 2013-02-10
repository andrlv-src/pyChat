# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui,  QtCore
import pychatgui_rc

class PyChatGui(QtGui.QMainWindow):
    ap=''
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(800, 240)
        self.setWindowTitle('Zu')
    
        self.chatLog = QtGui.QTextEdit()
        self.chatLog.setReadOnly(True)
        self.setCentralWidget(self.chatLog)
        
        self.createActions()
        self.createMenus()
        self.createToolbars()
        self.createDockWindows()
        self.createchatInputLine()
        self.createStatusBar()

        # получаем путь к нашему файлу
        self.ap = os.getcwdu()
        # подставляем к пути к картинке
        self.setChatLog(u'<b>тест</b>' + '<img src="' + self.ap + '\PyChatGUI\icons\mmmm.gif">')


    def createActions(self):
        self.quitAction = QtGui.QAction("&Quit", self, shortcut="Ctrl+Q",
        statusTip="Quit the application", triggered=self.close)
        self.arrowAction = QtGui.QAction(QtGui.QIcon(':/icons/arrow.png'), '&Enter message here',  self)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)
        self.viewMenu = self.menuBar().addMenu("&View")
        self.propertiesMenu = self.menuBar().addMenu("&Properties")
        self.aboutMenu = self.menuBar().addMenu("&About")
        
    def createToolbars(self):
        self.chatInputLineToolbar = QtGui.QToolBar()
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.chatInputLineToolbar)
        self.chatInputLineToolbar.setAllowedAreas(QtCore.Qt.BottomToolBarArea | QtCore.Qt.TopToolBarArea)
        self.chatInputLineToolbar.addAction(self.arrowAction)
        
    def createDockWindows(self):
        dock = QtGui.QDockWidget('Users', self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.userList = QtGui.QListWidget(dock)
        self.userList.addItems((
            u'Astartes',
            u'ПАЗДЪ',
            u'Благороднэ_Графэ_Дэ_Котэ'))
        dock.setWidget(self.userList)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

    def createchatInputLine(self):
        self.chatInputLine = QtGui.QLineEdit()
        self.chatInputLineToolbar.addWidget(self.chatInputLine)
        self.chatInputLine.connect(self.chatInputLine, QtCore.SIGNAL('returnPressed()'), self.getStringFromInputLine)
        
    def createStatusBar(self):
        self.statusBar().showMessage(u'Вэлкам!')






    # вносим текстовую строку в основное окно чат-лога
    def setChatLog(self, string):
        self.chatLog.append(string)
        print '->[debug]' + string

    # получаем строку из chatInputLine
    def getStringFromInputLine(self):
        chatInputLineContent = self.chatInputLine.text()
        self.setChatLog('[debug]' + chatInputLineContent)
        self.clearChatInputLine()
        self.emit(QtCore.SIGNAL('getStringFromInputLine')) # эмитит сиглал в основную программу
        return chatInputLineContent

        # TODO после копипасты не стирает почему-то, исправить
        # каким-то образом при копипасте копируется стиль написания скопипасченного текста
        


    def clearChatInputLine(self):
        self.chatInputLine.setText('')


    def getTextOutside(self):
        a = self.getStringFromInputLine()
        # self.emit(QtCore.SIGNAL('setText(QString)'),self.??????)

    def setText(self, string):
        self.setChatLog(string)

    def test_1(self, qwe):
        self.chatLog.append(qwe)
        





if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = PyChatGui()
    main.show()
    main.setChatLog(u'<b><p style="color:#0000ff">' + main.ap + '</p></b>')
    main.setChatLog(u'<b><p style="color:#0000ff">' + main.ap + '</p></b>')
    main.setChatLog(u'<b>тест</b>' + '<img src="' + main.ap + '\icons\WH40K.gif">')
    sys.exit(app.exec_())
