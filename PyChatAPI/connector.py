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
		self.connect_to_server()

	# соединение с сервером
	def connect_to_server(self):

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

	def receive_msg_from_server(self):
		return self.sock.recv(1024)

	def send_msg_to_server(self, string):
		self.sock.send(string)

if __name__ == '__main__':
	c = Connector()
	a = True
	while a:
		print c.receive_msg_from_server()