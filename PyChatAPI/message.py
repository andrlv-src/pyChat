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
	__parameters = ()


	def __init__(self, sender, command, parameters):
		self.__sender = sender
		self.__command = command
		self.__parameters = parameters

	# получить источник сообщения
	def get_sender(self):
		return self.__sender
	
	# получить коммаду
	def get_command(self):
		return self.__command

	# получить параметры комманды
	def get_parameters(self):
		return self.__parameters

if __name__=='__main__':
	print 'Message by WoenZu 2012'
	print 'version v0.0.2'
	raw_input('Press enter for exit...')
