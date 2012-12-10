# -*- coding: utf-8 -*-

import os, sys
from PyQt4 import QtGui,  QtCore
import pychatgui_rc

class PyChatGui(QtGui.QMainWindow):
    ap=''
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(800, 300)
        self.setWindowTitle('Zu')
    
        self.chatLog = QtGui.QTextEdit()
        self.chatLog.setReadOnly(True)
        self.setCentralWidget(self.chatLog)
        
        self.createActions()
        self.createMenus()
        self.createToolbars()
        self.createDockWindows()
        self.createChatImputLine()
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
        
    def createToolbars(self):
        self.chatImputLineToolbar = QtGui.QToolBar()
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.chatImputLineToolbar)
        self.chatImputLineToolbar.setAllowedAreas(QtCore.Qt.BottomToolBarArea | QtCore.Qt.TopToolBarArea)
        self.chatImputLineToolbar.addAction(self.arrowAction)
        
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

    def createChatImputLine(self):
        self.chatImputLine = QtGui.QLineEdit()
        self.chatImputLineToolbar.addWidget(self.chatImputLine)
        # подключаем поле для ввода к методу getLine()
        self.chatImputLine.connect(self.chatImputLine, QtCore.SIGNAL('returnPressed()'), self.getLine)
        
    def createStatusBar(self):
        self.statusBar().showMessage(u'Вэлкам!')

    # вносим текстовую строку в основное окно чат-лога
    def setChatLog(self, string):
        self.chatLog.append(string)
        print '->' + string

    # получаем строку из chatImputLine
    def getLine(self):
        self.setChatLog(self.chatImputLine.text())

        # TODO после копипасты не стирает почемута, исправить
        # каким-то образом при копипасте копируется стиль написания скопипасченного текста
        self.chatImputLine.setText('')
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = PyChatGui()
    main.show()
    main.setChatLog(u'<b><p style="color:#0000ff">' + main.ap + '</p></b>')
    main.setChatLog(u'<b><p style="color:#0000ff">' + main.ap + '</p></b>')
    main.setChatLog(u'<b>тест</b>' + '<img src="' + main.ap + '\icons\WH40K.gif">')
    sys.exit(app.exec_())
