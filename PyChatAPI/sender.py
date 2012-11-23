# -*- coding: utf-8 -*-
# pyChat by Zu
# 15.11.2012
# sender 

import rc4crypt
import message

class Sender(object):

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


