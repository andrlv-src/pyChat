# -*- coding: utf-8 -*-
# 12.12.2012
# CONNECT message

import message

class ConnectMsg(message.Message):
	
	def __init__(self, sender, command, parameters):
		message.Message.__init__(self, sender, command, parameters)

	def run(self):
		# в ГУИ посылаем строку отправитель параметры
		self.__string_to_gui = (str(self.get_sender()) + str(self.get_parameters()))

		# на сервер отправляем ''
		self.__string_to_srv = str('')

		# возвращаем кортэж строк
		return (self.__string_to_gui, self.__string_to_srv)

if __name__ == '__main__':
	print 'ConnectMsg'
	a = ConnectMsg('sender', 'command', ['param1', 'param2', 'param3'])
	print a.get_string()
	print a.run()