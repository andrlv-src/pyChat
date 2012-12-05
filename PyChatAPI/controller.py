# -*- coding: utf-8 -*-
# 05.12.2012

# FORWARD, CONNECT, DISCONNECT, CREATE_LINE, REFRESH, STATUS_REQ, 
		# STATUS, BOARD, TEXT, ME, RECEIVED, REFRESH_BOARD, RENAME, ALERT, CREATE;
		command = self.message.get_command()


		try:
			if command == 'CONNECT':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'DISCONNECT':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'CREATE_LINE':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'REFRESH':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'STATUS_REQ':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'STATUS':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'BOARD':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'TEXT':
				print self.PROMPT + '<%s>' % self.message.get_sender(), self.message.get_parameters()[1].decode('cp1251')
			elif command == 'ME':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'RECEIVED':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'REFRESH_BOARD':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'RENAME':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'ALERT':
				print '-*-', self.message.get_command(), self.message.get_parameters()
			elif command == 'CREATE':
				print '-*-', self.message.get_command(), self.message.get_parameters()

		except Exception, e:
			pass