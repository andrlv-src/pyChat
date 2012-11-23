# -*- coding: utf-8 -*-
# pyChat by Zu
# 31.10.2012
# listener 

import rc4crypt
import message

class Listener(object):

	def __init__(self):
		pass

	# развертываем сообщение с сервера
	def unwrap_server_message(self, message_obj): pass

	# развертываем сообщение от клиента
	def unwrap_client_message(self, message_obj): pass

	# шифруем сообщение
	# def crypt_message(self, message_obj): pass

	# дешифруем сообщение
	def decrypt_message(self, message_obj): pass

	# интерпретируем дешифровнную текстовую строку
	def string_processor(self, message_obj): pass







