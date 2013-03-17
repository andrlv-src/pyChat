# -*- coding: utf-8 -*-
# pyChat by Zu
# 28.10.2012
# message class
# контейнер для сообщения


class Message(object):

	__sender = ''
	__command = ''
	__parameters = []


	def __init__(self, sender, command, parameters):
		self.__sender = sender
		self.__command = command
		self.__parameters = parameters

	# запуск обработки сообщения
	def run(): 
		# должно возвращать словарь из двух параметров
		# первый сообщение на сервер, второй вывод в ГУИ
		# если параметр не дорлжен передаваться - сделать его пустым ''
		# при прочтении такого параметра другими объектами он должен игнорироваться\
		# return some(param to GUI, param to SRV)
		pass

	def get_sender(self):
		return self.__sender
	
	def get_command(self):
		return self.__command

	def get_parameters(self):
		return self.__parameters

	def get_string(self):
		return str(self.__sender + ' ' + self.__command + ' ' + ' '.join(self.__parameters))

if __name__=='__main__':
	print 'Message by WoenZu 2012'
	print 'version v0.0.2'
	raw_input('Press enter for exit...')
