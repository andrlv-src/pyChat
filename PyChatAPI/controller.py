# -*- coding: utf-8 -*-
# 05.12.2012

import defaultmsgprocessor
import connector

class Controller(object):


	def __init__(self):
		self.message_processor = defaultmsgprocessor.DefaultMsgProcessor()
		self.connector = connector.Connector()

	def listen_server(self):
		received_string = self.connector.receive_msg_from_server()
		message_object = self.message_processor.process_message(received_string)
		return message_object.run()

	def send_message_to_server(self, string_for_send): pass

if __name__ == '__main__':
	Controller()







# 	Список команд, их параметров и соответствующих им классов приведен ниже (формат {Команда [[0x13][0x13] параметры]}) :
#     ALERT [0x13][0x13] [текст сообщения] — алерт-сообщение (клиент может быть настроен на различные действие при получении алертов от пользователей). Класс IChatAlertMessage.
#     BOARD [0x13][0x13] [номер блока, начиная с нуля] [0x13][0x13] [текс блока] — сообщение для доски объявлений. Сообщения разбиваются на блоки по 300 (?) символов каждый. Класс IChatBoardMessage.
#     CONNECT [0x13][0x13] [Имя линии] [0x13][0x13] [логин пользователя] [0x13][0x13] [никнейм] [0x13][0x13] [не используется] [0x13][0x13] [0x13][0x13] [приветственное сообщение] [0x13][0x13] [получатель] [0x13][0x13] [версия] [0x13][0x13] [статус] — сообщение о подключении (как к общему чату, так и к линии). Поле получателя играет особую роль. При подключении клиент отправляет сообщение о подключении с полем получателя равным "*". Получив такое сообщение каждый клиент в свою очередь отправляет ответное сообщение о подключении с полем получателя, равным IDENT’у нашего клиента. Таким образом, необходимо анализировать это поле для того чтобы вовремя отправить сообщение о собственном подключении, иначе мы не попадём в список контактов новоподключившегося клиента. Класс IChatConnectMessage.
#     CREATE_LINE [0x13][0x13] [имя линии] [пароль для входа в линию] [отправитель] — создание линии. Класс IChatCreateLineMessage.
#     CREATE [0x13][0x13] [идентификатор приватной линии] [0x13][0x13] [не используется?] [0x13][0x13] [получатель] — создание личного чата. Класс IChatCreateMessage.
#     DISCONNECT [0x13][0x13] [имя линии] — выход из линии. Класс IChatDisconnectMessage.
#     ME [0x13][0x13] [сообщение] [0x13][0x13] [имя линии] [0x13][0x13] [получатель] — аналог ACTION в IRC (команда /me сообщение). Класс IChatMeMessage.
#     RECEIVED [0x13][0x13] [имя линии] [0x13][0x13] [текст подтверждения] — подтверждение получения сообщения. Класс IChatReceivedMessage.
#     REFRESH_BOARD — запрос на обновление доски объявлений. Класс IChatRefreshBoardMessage.
#     REFRESH [0x13][0x13] [имя линии] [0x13][0x13] [логин пользователя] [0x13][0x13] [никнейм] [0x13][0x13] [не используется] [0x13][0x13] [приветствие] [0x13][0x13] [получатель] [0x13][0x13] [версия] [0x13][0x13] [статус] — обновление списка контактов. Как и в случае с CONNECT, поле «получатель» несёт особую нагрузку. Клиент периодически отправляет запрос на обновление списка контактов, в этом случае поле получатель будет содержать "*" (звёздочку). В ответ на это сообщение каждый клиент, подключённый к данной линии должен отправить ответное REFRESH сообщение, но в поле «получатель» будет содержаться IDENT нашего клиента. Таким образом, опять же, нам необходимо анализировать это поле чтобы вовремя сигнализировать запрашивающему клиенту о своём присутствии на линии. Класс IChatRefreshMessage.
#     RENAME [0x13][0x13] [новый никнейм] — сообщение о смене имени пользователя. Класс IChatRenameMessage.
#     STATUS [0x13][0x13] [новый статус] [0x13][0x13] [сообщение статуса] — сообщение о смене пользователем статуса. «Сообщение статуса» — сообщение, которое будет выдано пользователю в ответ на попытку отправить личное сообщение. Класс IChatStatusMessage.
#     STATUS_REQ — запрос статуса пользователя. Класс IChatStatusReqMessage.

#     TEXT [0x13][0x13] [имя линии] [0x13][0x13] [текст сообщения] [0x13][0x13] [имя получателя (не IDENT)] — текст сообщения. 
#     	Вид сообщения (общее или личное регулируется с помощью имени линии, см. ниже). Обратите внимание на то, что имя
#		получателя в данном случае — это НЕ IDENT-строка. Это обращение, которое будет указано в теле сообщения, выводимого
#		пользователю (в случае личного сообщения). Имя пользователя для личного сообщения может быть любым. Для публичного 
#		сообщение поле обычно содержит "*" (звёздочку). Класс IChatTextMessage.

# Везде, где используется параметр «имя линии» используются следующие соглашения: для обозначения «общего чата» используется имя линии, равное «iTCniaM»; для обозначения «приватного сообщения» используется имя линии, равное «gsMTCI».