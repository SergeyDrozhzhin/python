
# coding: utf-8

from PyQt5.QtCore import pyqtSignal, QDateTime
from PyQt5.QtWidgets import QDialog, QDataWidgetMapper
# from PyQt5.uic import loadUi

from .ui.Ui_LoginWidget import Ui_LoginWidget

class LoginWidget(QDialog, Ui_LoginWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_ui()
		#self.init_signals()

	def init_ui(self):
		self.setupUi(self)


			

		

