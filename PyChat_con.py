# -*- coding: utf-8 -*-
# 03.02.2013


## TODO разобраться с относительностью путей к смайлам после преобразования py2exe 
##      иное решение - настройка пути к файлам смайлов в самом чате

import sys
import time
from PyQt4 import QtGui,  QtCore
import PyChatAPI.connector
import PyChatAPI.defaultmsgprocessor
import PyChatGUI.pychatgui

def main():
	app = QtGui.QApplication(sys.argv)
	gui = PyChatGUI.pychatgui.PyChatGui()
	pychat = PyChat()
	gui.connect(pychat, QtCore.SIGNAL('putStringInChatLog'), gui.putStringInChatLog)
	pychat.connect(gui, QtCore.SIGNAL('getStringFromInputLine'), pychat.send_message_to_server)
	
	gui.show()
	pychat.start()  
	sys.exit(app.exec_())

class PyChat(QtCore.QThread):

	def __init__(self, parent=None):
		QtCore.QThread.__init__(self, parent)
		self.message_processor = PyChatAPI.defaultmsgprocessor.DefaultMsgProcessor()
		self.connector = PyChatAPI.connector.Connector()

	def run(self):
		main_loop = True
		while main_loop:
			self.listen_server()

	def listen_server(self):
		received_string = self.connector.receive_msg_from_server()
		message_object = self.message_processor.process_message(received_string)
		self.process_message_content(message_object)

	def process_message_content(self, message_object):
		dictionary_actions = message_object.run()
		if 'GUI' in dictionary_actions:
			self.emit(QtCore.SIGNAL('putStringInChatLog'), dictionary_actions.get('GUI').decode('cp1251'))
		if 'SERVER' in dictionary_actions:
			pass


	def send_message_to_server(self, string_for_send):
		# processor
		# connector
		pass

if __name__ == '__main__':
	main()
