# -*- coding: utf-8 -*-
# 31.10.2012
# WoenZu

import msgprocessor
import rc4crypt
import message
import sys

class DefaultMsgProcessor(msgprocessor.MsgProcessor): # message processor
	
	# ключ для штфратора/дешифратора
	KEY = b'tahci'

	# разделители
	SEPARATOR = '\x13'
	ZERO_SEPARATOR = '\x00'

	# входящая строка
	# msg_string = ''

	# развернутое сообщение
	unwrapped_msg = ''

	# расшифрованное сообщение
	decrypted_msg = ''


	def __init__(self):

		# создаем объект "шифровщик"
		self.rc4_coder = rc4crypt.RC4Crypt()

		# создаем объект "сообщение"
		# self.message = message.Message(None, None, None)

	# обработчик полученного сообщения
	def process_message_from_server(self, msg_string):
			
		# снимаем враппер
		self.unwrapped_msg = self.unwrap_server_message(msg_string)

		# дешифруем текстовое сообщение посредством RC4
		self.decrypted_msg = self.decrypt_message(self.unwrapped_msg)

		# обрабатываем дешифрованное текстовое сообщение и возвращаем его в виде объекта message
		return self.string_processor(self.decrypted_msg)

	def process_message_from_client(self, msg_string): 
		# снимаем враппер
		# дешифруем текстовое сообщение посредством RC4
		# обрабатываем дешифрованное текстовое сообщение и возвращаем его в виде объекта message
		pass

	def build_message_to_server(): pass

	def build_message_to_client(): pass

	# развертываем сообщение с сервера
	def unwrap_server_message(self, rec_msg):
		# Формат сообщения, отправляемого сервером клиенту:
		# [Длина сообщения] [0x00] [Команда] [0x00] [Сообщение]

		pos = []
		for i in range(len(rec_msg)):
			if rec_msg[i] == self.ZERO_SEPARATOR:
				pos.append(i)

		# возвращаем [сообщение]
		return rec_msg[pos[1]+1:]

	# развертываем сообщение от клиента
	def unwrap_client_message(self, message_obj): pass

	# завертываем сообщение с сервера
	def wrap_server_message(self, message_obj): pass

	# завертываем сообщение от клиента
	def wrap_client_message(self, message_obj): pass
	
	# шифруем сообщение
	def crypt_message(self, msg):
		return self.decrypt_message(msg)

	# дешифруем текстовое сообщение
	def decrypt_message(self, msg):
		msg = self.rc4_coder.cipher(msg, self.KEY)
		return msg

	# интерпретируем/истолковываем дешифрованную текстовую строку
	def string_processor(self, msg):
		# формат обрабатываемого сообщения
		# [0x13] "ichat" [0x13] [0x13] [Счетчик ASCII] [0x13][0x13] [Отправитель] [0x13][0x13]
		# [Команда] [0x13][0x13] [параметры команды] [0x13]

		msg = msg.split(self.SEPARATOR)
		param= []
		while '' in msg:
			msg.remove('')

		for i in range(4, len(msg)):
			param.append(msg[i])

		# TODO проверка на сообщение, правильный ли формат
		return message.Message(msg[2], msg[3], param)



if __name__ == '__main__':
	print '-> class default message processor, test...'
	x = '61\x00FORWARD\x00\x0b\xc2c\x0c\xc1a\x9f@\xd5\xef\x98k\xeb\xd5\x19\x16\x12\xe1\xc4^\xa3\x8eEw\xc2P\xa5\x07\xec\xdb\xe36\xc7\xa0\xab\x9aW\xf5X\x95S\x9fG\xb3\xec6\xd0\xfb5eh4o'
	print '-> processing string: \n', '->', x
	a = DefaultMsgProcessor()
	returned_str =  a.process_message_from_server(x)
	print '-> output', returned_str.get_string()
	raw_input('-> press Enter to Exit...')

