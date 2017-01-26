# coding: utf-8
# Drozhzhin S.I.

from PyQt5.QtWidgets import QMainWindow, QApplication, QMainWindow, QWidget, QLabel, QPushButton, QDoubleSpinBox, QVBoxLayout, QMessageBox 
from .ui.Ui_MainWindow import Ui_MainWindow
from .NotesWidget import NotesWidget
from .LoginWidget import LoginWidget
from core.NoteModel import NoteModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.init_ui()
        self.init_signals()

    def init_ui(self):
        self.setupUi(self)

       
        self.notesWidget = NotesWidget(NoteModel(self), self)
        self.loginWidget=LoginWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.notesWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)

    def init_signals(self):
        self.actionAdd.triggered.connect(
            self.notesWidget.add_new_note
        )
        self.actionExit.triggered.connect(self.close)

        self.actionEdit.triggered.connect(
            self.notesWidget.edit_selected_note
        )
        self.actionRemove.triggered.connect(
            self.notesWidget.remove_selected_notes
        )

        self.notesWidget.selection_changed.connect(
            self.update_menu
        )

        self.loginWidget.okBtn.clicked.connect(self.onClickProverka)
        

    def update_menu(self):
        selected = self.notesWidget.selected_rows()
        self.actionEdit.setEnabled(len(selected) == 1)
        self.actionRemove.setEnabled(bool(selected))
       


    def onClickProverka(self):
        valueLogin = self.loginWidget.loginEdit.text()
        valuePassword=self.loginWidget.passwordEdit.text()

        if valueLogin!='admin' and valuePassword!='admin':
            buttonReply = QMessageBox.warning(self, 'Внимание', "Нужно ввести корректные логин и пароль!", QMessageBox.Yes)
        else:
            self.stackedWidget.setCurrentWidget(self.notesWidget)
            self.toolBar.setEnabled(True)
