# -*- coding: utf-8 -*-
# pyChat by Zu
# 31.10.2012
# message processor 

import rc4encoder

class MsgProcessor(object):

	def __init__(self):
		pass

	# развертываем сообщение с сервера
	def unwrap_message_from_server(self, message_obj): pass

	# развертываем сообщение от клиента
	def unwrap_message_from_client(self, message_obj): pass

	# завертываем сообщение с сервера
	def wrap_message_to_server(self, message_obj): pass

	# завертываем сообщение от клиента
	def wrap_message_to_client(self, message_obj): pass

	# шифруем сообщение
	def crypt_message(self, msg): pass

	# дешифруем сообщение
	def decrypt_message(self, msg): pass

	# интерпретируем дешифровнную текстовую строку
	def build_message_object(self, message): pass

	
