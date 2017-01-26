# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_widget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(215, 114)
        self.gridLayout = QtWidgets.QGridLayout(LoginWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(LoginWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(LoginWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginEdit = QtWidgets.QLineEdit(LoginWidget)
        self.loginEdit.setObjectName("loginEdit")
        self.verticalLayout.addWidget(self.loginEdit)
        self.passwordEdit = QtWidgets.QLineEdit(LoginWidget)
        self.passwordEdit.setObjectName("passwordEdit")
        self.verticalLayout.addWidget(self.passwordEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        self.okBtn = QtWidgets.QPushButton(LoginWidget)
        self.okBtn.setObjectName("okBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.okBtn)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "Dialog"))
        self.label.setText(_translate("LoginWidget", "Логин"))
        self.label_2.setText(_translate("LoginWidget", "Пароль"))
        
        self.okBtn.setText(_translate("LoginWidget", "Ок"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWidget = QtWidgets.QDialog()
    ui = Ui_LoginWidget()
    ui.setupUi(LoginWidget)
    LoginWidget.show()
    sys.exit(app.exec_())

