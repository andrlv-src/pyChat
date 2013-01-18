# -*- coding: utf-8 -*-
# pychat for consolr
# for test
# 17.01.2013


import sys
import threading
import PyChatAPI.defaultmsgprocessor
import PyChatAPI.connector
import PyChatGUI.pychatgui

class PyChat(object):
	def __init__(self):

		ml = MainLogic()
		ml.start()
		self.ss()

	def ss(self):
		loop = True
		while loop:
			a = raw_input()
			if a == 'q':
				loop = False


class MainLogic(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		print 'second thread started...'
		main_loop = True
		while main_loop:
			pass



        
if __name__ == '__main__':
    PyChat()