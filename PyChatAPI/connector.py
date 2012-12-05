# -*- coding: utf-8 -*-
# connector class
# 05/12/2012

import socket

# создаем сокет
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


		# подсоединяемся к чат-серверу
		self.connect()

	# соединение с сервером
	def connect(self):

		# TODO проверку на коннект try/except
		HOST = 'localhost'
		# HOST = '10.1.9.93'	# адрес сервеоа
		PORT = 6666			# порт вервера
		print self.PROMPT + 'connecting to %s...' % HOST

		try:
			self.sock.connect((HOST, PORT))
			print self.PROMPT + 'connected at', HOST,':', PORT
		except Exception, e:
			print self.PROMPT + 'unable to connect at', HOST,':', PORT
			raw_input('press enter')
			exit(0)