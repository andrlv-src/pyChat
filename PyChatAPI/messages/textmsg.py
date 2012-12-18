# -*- coding: utf-8 -*-
# 12.12.2012
# TEXT message

import message

class TextMsg(message.Message):
	
	def __init__(self, sender, command, parameters):
		message.Message.__init__(self, sender, command, parameters)

	def run(self):
		# в ГУИ посылаем строку отправитель параметры
		self.__string_to_gui = (str(self.get_sender()) + str(self.get_parameters()))

		# на сервер отправляем ''
		self.__string_to_srv = str('')

		# возвращаем кортэж строк
		return {'GUI' : self.__string_to_gui, 
				'SERVER' : self.__string_to_srv}

if __name__ == '__main__':
	print 'TextMsg'
	a = TextMsg('sender', 'command', ['param1', 'param2', 'param3'])
	print a.get_string()
	print a.run()



	