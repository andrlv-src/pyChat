# -*- coding: utf-8 -*-
# pyChat by Zu
# 28.10.2012
# message class
# контейнер для сообщения


class Message(object):

	# источник сообщения
	__sender = ''

	# команда
	__command = ''

	# параметры комманды
	__parameters = []


	def __init__(self, sender, command, parameters):
		self.__sender = sender
		self.__command = command
		self.__parameters = parameters

	# запуск обработки сообщения
	def run(): 
		# должно возвращать кортэж из двух параметров
		# первый сообщение на сервер, второй вывод в ГУИ
		# если параметр не дорлжен передаваться - сделать его пустым ''
		# при прочтении такого параметра другими объектами он должен игнорироваться\
		# return some(param to GUI, param to SRV)
		pass

	# получить источник сообщения
	def get_sender(self):
		return self.__sender
	
	# получить коммаду
	def get_command(self):
		return self.__command

	# получить параметры комманды
	def get_parameters(self):
		return self.__parameters

	# tostring
	def get_string(self):
		return str(self.__sender + ' ' + self.__command + ' ' + ' '.join(self.__parameters))

if __name__=='__main__':
	print 'Message by WoenZu 2012'
	print 'version v0.0.2'
	raw_input('Press enter for exit...')