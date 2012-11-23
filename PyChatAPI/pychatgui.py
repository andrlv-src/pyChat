# -*- coding: utf-8 -*-
# 15.11.2012
# WoenZu
# pyChat GUI

from Tkinter import *

class PyChatGUI(object):

	def __init__(self):
		self.root=Tk()

		self.root.title('Наш замечательный ФИПСочятик alpha version')
		self.root.geometry('600x300')
		# root.wm_iconbitmap('MyIcon.ico')


		self.log_scrollbar = Scrollbar(self.root)
		self.log_scrollbar.pack(side=RIGHT, fill=Y)

		self.user_list_scrollbar = Scrollbar(self.root)
		self.user_list_scrollbar.pack(side=RIGHT, fill=Y)

		# создаем основное окно чата
		self.log_window = Text(self.root, yscrollcommand=self.log_scrollbar.set)
		self.log_scrollbar.config(command=self.log_window.yview)

		# создаем юзер-лист
		self.user_list = Listbox(self.root, yscrollcommand=self.user_list_scrollbar.set)
		self.user_list_scrollbar.config(command=self.user_list.yview)

		# создаем переменную для вводимого текста
		self.console_var = StringVar()
		self.console_var.set('')

		self.console = Entry(self.root, textvariable=self.console_var)
		self.console.pack(side='bottom', fill='x', expand='true')		
		self.log_window.pack(side='left', fill='both', expand='true')
		self.user_list.pack(side='right', fill='both', expand='true')		



		self.log_window.configure(state='disabled')

		self.root.mainloop()




	def main(self):
		pass

	def function(self):
		pass

if __name__ == '__main__':
	PyChatGUI()