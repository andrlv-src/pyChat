# -*- coding: utf-8 -*-
# 03.02.2013


## TODO разобраться с относительностью путей к смайлам после преобразования py2exe 
##      иное решение - настройка пути к файлам смайлов в самом чате

import sys
import time

from PyQt4 import QtGui,  QtCore
import PyChatAPI.controller
import PyChatGUI.pychatgui


def main():
	app = QtGui.QApplication(sys.argv)
	gui = PyChatGUI.pychatgui.PyChatGui()
	pychat = PyChat()
	gui.connect(pychat, QtCore.SIGNAL('setText(QString)'), gui.setText)
	pychat.connect(gui, QtCore.SIGNAL('getStringFromInputLine'), pychat.send_message_to_server)
	
	gui.show()
	pychat.start()  
	sys.exit(app.exec_())

class PyChat(QtCore.QThread):

	def __init__(self, parent = None):
		QtCore.QThread.__init__(self, parent)
		self.controller = PyChatAPI.controller.Controller()

	def run(self):
		main_loop = True
		while main_loop:
			self.listen_server()
			

	def sent_to_gui(self, string_for_send):
		# self.emit(QtCore.SIGNAL('setText(QString)'),self.string_for_send) # to GUI
		pass

	def listen_server(self):
		self.controller.listen_server()

	def send_message_to_server(self, message_for_send):
		self.controller.send_message_to_server(message_for_send)


if __name__ == '__main__':
	main()
