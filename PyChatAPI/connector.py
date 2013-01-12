# -*- coding: utf-8 -*-
# connector class
# 05.12.2012

import socket
import sys

class Connector(object):

	__HOST = 'localhost'
	__PORT = '6666'
	__observer = None

	def __init__(self):
		
		# создаем сокет
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# подсоединяемся к чат-серверу
		self.connect()

	# соединение с сервером
	def connect(self):

		HOST = 'localhost'
		# HOST = '10.1.9.93'	# адрес сервеоа
		PORT = 6666			# порт вервера
		print 'connecting to %s...' % HOST

		try:
			self.sock.connect((HOST, PORT))
			print 'connected at', HOST,':', PORT
		except Exception, e:
			print 'unable to connect at', HOST,':', PORT
			try:
				raw_input('press enter')
			except (EOFError):
				sys.exit(0)

	def receive(self):
		return self.sock.recv(1024)

	def send(self, string):
		pass

	def registerObserver(self, observer_obj):
		self.__observer = controller_obj

	def reportObserver(self):
		pass
		
if __name__ == '__main__':
	c = Connector()
	a = True
	while a:
		print c.receive()