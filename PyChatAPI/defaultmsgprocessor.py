# -*- coding: utf-8 -*-
# 31.10.2012
# WoenZu
# decode('cp1251')

import msgprocessor
import rc4encoder
import sys

import messages.alertmsg
import messages.boardmsg
import messages.connectmsg
import messages.createlinemsg
import messages.createmsg
import messages.disconnectmsg
import messages.memsg
import messages.receivedmsg
import messages.refreshboardmsg
import messages.refreshmsg
import messages.renamemsg
import messages.statusmsg
import messages.statusreqmsg
import messages.textmsg

class DefaultMsgProcessor(msgprocessor.MsgProcessor):
	
	# ключ для штфратора/дешифратора
	KEY = b'tahci'
	SEPARATOR = '\x13'
	ZERO_SEPARATOR = '\x00'

	def __init__(self):
		self.rc4_encoder = rc4encoder.RC4Encoder()

	def process_message(self, msg_string):
		message = self.unwrap_message_from_server(msg_string)
		message = self.decrypt_message(message)
		new_message_object = self.build_message_object(message)
		return new_message_object

	def unwrap_message_from_server(self, msg_for_unwrapping):
		# Формат сообщения, отправляемого сервером клиенту:
		# [Длина сообщения] [0x00] [Команда] [0x00] [Сообщение]
		pos = []
		for i in range(len(msg_for_unwrapping)):
			if msg_for_unwrapping[i] == self.ZERO_SEPARATOR:
				pos.append(i)
		return msg_for_unwrapping[pos[1]+1:]

	def decrypt_message(self, msg_for_decrypting):
		return self.rc4_encoder.encode(msg_for_decrypting, self.KEY)

	def build_message_object_to_server(): pass

	def crypt_message(self, msg):
		return self.decrypt_message(msg)

	def wrap_message_to_server(self, message_obj): pass

	# интерпретируем/истолковываем дешифрованную текстовую строку
	def build_message_object(self, msg):
		# формат обрабатываемого сообщения
		# [0x13] "ichat" [0x13] [0x13] [Счетчик ASCII] [0x13][0x13] [Отправитель] [0x13][0x13]
		# [Команда] [0x13][0x13] [параметры команды] [0x13]

		# FORWARD, *CONNECT, *DISCONNECT, *CREATE_LINE, *REFRESH, *STATUS_REQ, 
		# *STATUS, *BOARD, *TEXT, *ME, *RECEIVED, *REFRESH_BOARD, *RENAME, *ALERT, *CREATE;

		# TODO проверка на сообщение, правильный ли формат 
		# msg[2] = __sender, msg[3] = __command

		msg = msg.split(self.SEPARATOR)
		while '' in msg:
			msg.remove('')

		parameters = []
		for i in range(4, len(msg)):
			parameters.append(msg[i])

		sender = msg[2]
		command = msg[3]
		constructed_message = self.construct_message(sender, command, parameters)
		return constructed_message

	def construct_message(self, sender, command, parameters):
		try:
			if command == 'CONNECT':
				return messages.connectmsg.ConnectMsg(sender, command, parameters)
			elif command == 'DISCONNECT':
				return messages.disconnectmsg.DisconnectMsg(sender, command, parameters)
			elif command == 'CREATE_LINE':
				return messages.createlinemsg.CreateLineMsg(sender, command, parameters)
			elif command == 'REFRESH':
				return messages.refreshmsg.RefreshMsg(sender, command, parameters)
			elif command == 'STATUS_REQ':
				return messages.statusreqmsg.StatusReqMsg(sender, command, parameters)
			elif command == 'STATUS':
				return messages.statusmsg.StatusMsg(sender, command, parameters)
			elif command == 'BOARD':
				return messages.boardmsg.BoardMsg(sender, command, parameters)
			elif command == 'TEXT':
				return messages.textmsg.TextMsg(sender, command, parameters)
			elif command == 'ME':
				return messages.memsg.MeMsg(sender, command, parameters)
			elif command == 'RECEIVED':
				return messages.receivedmsg.ReceivedMsg(sender, command, parameters)
			elif command == 'REFRESH_BOARD':
				return messages.refreshboardmsg.RefreshBoardMsg(sender, command, parameters)
			elif command == 'RENAME':
				return messages.renamemsg.RenameMsg(sender, command, parameters)
			elif command == 'ALERT':
				return messages.alertmsg.AlertMsg(sender, command, parameters)
			elif command == 'CREATE':
				return messages.createmsg.CreateMsg(sender, command, parameters)
		except Exception, e:
			print '[debug] Error: unknown command', e	

if __name__ == '__main__':
	print '-> class default message processor, test...'
	x = '61\x00FORWARD\x00\x0b\xc2c\x0c\xc1a\x9f@\xd5\xef\x98k\xeb\xd5\x19\x16\x12\xe1\xc4^\xa3\x8eEw\xc2P\xa5\x07\xec\xdb\xe36\xc7\xa0\xab\x9aW\xf5X\x95S\x9fG\xb3\xec6\xd0\xfb5eh4o'
	print '-> processing string: \n', '->', x
	a = DefaultMsgProcessor()
	message_obj =  a.process_message(x)
	print '-> object: ', message_obj
	print '-> output: ', message_obj.run()
	try:
		raw_input('-> press Enter to Exit...')
	except (EOFError):
		sys.exit(0)