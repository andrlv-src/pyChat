# -*- coding: utf-8 -*-
# 12.12.2012
# TEXT message

import message

class TextMsg(message.Message):
	
	def __init__(self, sender, command, parameters):
		message.Message.__init__(self, sender, command, parameters)

	def run(self):
		string_of_parameters = ' '.join(self.get_parameters())
		string_for_gui = (self.get_sender() + ' ' + string_of_parameters)
		string_for_srv = str('')

		return {'GUI' : string_for_gui, 
				'SERVER' : string_for_srv}

if __name__ == '__main__':
	print 'TextMsg'
	a = TextMsg('sender', 'command', ['param1', 'param2', 'param3'])
	print a.run()