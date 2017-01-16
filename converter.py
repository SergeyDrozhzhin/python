#CurrencyExchange
#Drozhzhin_Sergey

import sys
from PyQt5.QtCore import QObject#spin дробное число
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QDoubleSpinBox, QVBoxLayout, QMessageBox )

class Course(QObject): #наследуем от ку обжект, чтобы получить все возможности от ку обжекта
		def get(self):
			return 30.0


	
class CurrencyConverter(QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.unitUi()
		self.initSignals()
		self.initLayouts()
		
	def unitUi(self): 

		self.setWindowTitle('Конвертер валют')
			#Интерфейс
		self.srcLabelRur=QLabel('Сумма в рублях', self)
		self.srcLabelUsd= QLabel("Сумма в долларах", self)

		self.srcAmountRur= QDoubleSpinBox(self) #у дабл спин бокс один конструктор (см документацию)
		self.srcAmountRur.setMaximum(999999999) #максмально допустимое значение для ввода

		self.srcAmountUsd=QDoubleSpinBox(self)
		self.srcAmountUsd.setMaximum(999999999)

		#Кнопка
		self.convertBtn=QPushButton('Перевести')
		self.cleanBtn=QPushButton('Очистить')
		self.convertBtn.setEnabled(False)
		#self.resultAmount.setReadOnly(True)
		pass
	def initSignals(self): #обработчики сигналов
		self.convertBtn.clicked.connect(self.onClick)
		self.cleanBtn.clicked.connect(self.clean)
		self.srcAmountUsd.valueChanged.connect(self.check)
		self.srcAmountRur.valueChanged.connect(self.check)
		
		pass

	def initLayouts(self):
		self.w= QWidget() #вспоогательный, промежуточный, и мы его сделаем центральным
		#делаем слои
		self.mainLayout = QVBoxLayout(self.w) #когда мы передаём в слой в виджет (по сути мы назначем виджету слой)
		self.mainLayout.addWidget(self.srcLabelRur)
		self.mainLayout.addWidget(self.srcAmountRur)
		self.mainLayout.addWidget(self.srcAmountUsd)
		self.mainLayout.addWidget(self.srcLabelUsd)
		self.mainLayout.addWidget(self.convertBtn)
		self.mainLayout.addWidget(self.cleanBtn)

		self.setCentralWidget(self.w)
		pass		

	def check(self):
		self.convertBtn.setEnabled(True)
		


	def clean(self):
		self.srcAmountUsd.setValue(0)
		self.srcAmountRur.setValue(0)

	
	def keyPressEvent(self, e):
		if e.key() == 16777220 or key.key() == 16777221: 
			self.onClick()	


	def onClick(self):
		valueRur= self.srcAmountRur.value()
		valueUsd= self.srcAmountUsd.value()
		#для всех виджетов, которые хрянят цифры- метод value
		# случае с со строкой- метод текст. Есть и такие и сякие виджеты	
		if valueRur> 0 and valueUsd==0: #получаем курс из интернета
			self.srcAmountUsd.setValue(valueRur / Course().get())
			self.convertBtn.setEnabled(True)
		elif valueUsd >0 and valueRur==0:
			self.srcAmountRur.setValue(valueUsd * Course().get())
			self.convertBtn.setEnabled(True)
		elif valueRur==0 and valueUsd==0:
			buttonReply = QMessageBox.question(self, 'Внимание', "Вы не ввели значение!", QMessageBox.Yes)
			self.convertBtn.setEnabled(False)
			print(int(buttonReply))
		else:
			buttonReply = QMessageBox.question(self, 'Внимание', "Нужно очистить одно из полей!", QMessageBox.Yes)
			self.convertBtn.setEnabled(False)
			


			
        	

	
				



#процесс запуска
if __name__=='__main__':
	app=QApplication(sys.argv)
	converter=CurrencyConverter()
	converter.show()
	sys.exit(app.exec_())


#Cлои используются для компоновки виджетов\
#QLayout-
#QHBoxLayout- горизонтальный слой (в ряд друг за другом)
#QVBoxLayout- вертикальный (вертикально друг за другом)
#QFormLayout- форма. слой 2 колонки в одной лейбл, во второй элемент (подпись- элементт)
#QGridLayout- сетка. колонок много

#Блокировка. У любого виджета есть метод setEnabled. Если тру - вкл
#set readonly - только для виджетов, у которых есть текст

#ДЗ
#1 Доделать конвертер. Нужно сделать кнопку "Очистить" (документация по дабл спин бокс)
#2 Мы должны блокировать кнопку "Конвертировать", если в поле 0, кнопка должна менять в режиме онлайн
#3 Конвертер должен работать в обе стороны.
# Конвертер если

#посмотреть классную библиотеку lxml

#ДЗ кидаем на гитхаб