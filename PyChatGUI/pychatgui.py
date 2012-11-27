# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,  QtCore
import pychatgui_rc

class PyChatGui(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.resize(800, 300)
        self.setWindowTitle('Zu')
    
        self.text_edit = QtGui.QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        self.create_actions()
        self.create_menus()
        self.create_toolbars()
        self.create_dock_windows()
        self.create_text_line()
        self.create_statusbar()        
    
    def create_actions(self):
        self.quit_act = QtGui.QAction("&Quit", self, shortcut="Ctrl+Q",
        statusTip="Quit the application", triggered=self.close)
        self.arrow_act = QtGui.QAction(QtGui.QIcon(':/icons/arrow.png'), '&Enter message here',  self)

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu("&File")
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_act)
        self.viewMenu = self.menuBar().addMenu("&View")
        
    def create_toolbars(self):
        self.line_toolbar = QtGui.QToolBar()
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.line_toolbar)
        self.line_toolbar.setAllowedAreas(QtCore.Qt.BottomToolBarArea | QtCore.Qt.TopToolBarArea)
        self.line_toolbar.addAction(self.arrow_act)
        
    def create_dock_windows(self):
        dock = QtGui.QDockWidget('Users', self)
        dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea)
        self.customer_list = QtGui.QListWidget(dock)
        self.customer_list.addItems((
            'Astartes',
            u'ПАЗДЪ',
            u'Благороднэ_Графэ_Дэ_Котэ'))
        dock.setWidget(self.customer_list)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        self.viewMenu.addAction(dock.toggleViewAction())

#        self.customer_list.currentTextChanged.connect(self.insertCustomer)

    def create_text_line(self):
        self.line_edit = QtGui.QLineEdit()
        self.line_toolbar.addWidget(self.line_edit)
        
    def create_statusbar(self):
        self.statusBar().showMessage(u'Вэлкам!')
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = PyChatGui()
    main.show()
    sys.exit(app.exec_())
