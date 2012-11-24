# -*- coding: utf-8 -*-
# pyChat main class
# 31.10.2012
# WoenZu
# Chat client for iChat server

import socket

import listener
import rc4crypt
import message
import messages.text
class DefaultListener(listener.Listener): # listener
	
	# ключ для штфратора/дешифратора
	KEY = b'tahci'

	# разделители
	SEPARATOR = '\x13'
	ZERO_SEPARATOR = '\x00'

	PROMPT = '-*- '

	# полученное сообщение
	recieved_msg = ''

	# развернутое сообщение
	unwrapped_msg = ''

	# расшифрованное сообщение
	decrypted_msg = ''


	def __init__(self):

		# создаем сокет
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# создаем объект "шифровщик"
		self.rc4_coder = rc4crypt.RC4Crypt()

		# создаем объект "сообщение"
		# self.message = message.Message(None, None, None)

		# подсоединяемся к чат-серверу
		self.connect()

		# основной цикл
		self.process_received_message() 

	# обработчик полученного сообщения
	def process_received_message(self):
		
		life_cycle = True
		while life_cycle:
			
			self.recieved_msg = self.sock.recv(1024)	# просечь что за цифра	
			
			# снимаем враппер
			self.unwrapped_msg = self.unwrap_server_message(self.recieved_msg)

			# дешифруем текстовое сообщение посредством RC4
			self.decrypted_msg = self.decrypt_message(self.unwrapped_msg)

			# обрабатываем дешифрованное текстовое сообщение
			self.message = self.string_processor(self.decrypted_msg)



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



			# определяем его(сообщения) тип, сравнение команды, потом выбор интерпретатора для команды
			# слушатель отправляет сообщение на вывод, в соответствии с типом сообщения
			# вывод сообщения

			

			# TODO вторым потоком зускается второй основной цико с коммандной строкой


	# соединение с сервером
	def connect(self):

		# TODO проверку на коннект try/except
		HOST = 'localhost'
		# HOST = '10.1.9.93'	# адрес сервеоа
		PORT = 6666			# порт вервера
		print self.PROMPT + 'connecting to %s...' % HOST

		try:
			self.sock.connect((HOST, PORT))
			print self.PROMPT + 'connected at', HOST,':', PORT
		except Exception, e:
			print self.PROMPT + 'unable to connect at', HOST,':', PORT
			raw_input('press enter')
			exit(0)

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

		# TODO проверка на сообщение, правильный ди формат
		return message.Message(msg[2], msg[3], param)



if __name__ == '__main__':
	DefaultListener()

