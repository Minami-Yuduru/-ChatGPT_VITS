# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import real_basic_UI

class Ui_Dialog(object):
    def __init__(self,Dialog):
        self.Dialog = Dialog

    def setupUi(self):
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(398, 500)
        self.Dialog.setFixedSize(398, 500)


        self.label_speaker = QtWidgets.QLabel(self.Dialog)
        self.label_speaker.setGeometry(QtCore.QRect(30, 20, 111, 16))
        self.lineEdit_name = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(30, 50, 341, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.buttonBox = QtWidgets.QDialogButtonBox(self.Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 390+70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 40+70, 341, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20+70, 150, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 350+70, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 350+70, 31, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked_push_button)
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 320+70, 111, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.button_box_accepted)
        self.buttonBox.rejected.connect(self.Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_speaker.setText(_translate("Dialog", '对话角色名'))
        self.label.setText(_translate("Dialog", "设定文本"))
        self.pushButton.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "从文件中导入"))

    def clicked_push_button(self):
        path = QtWidgets.QFileDialog.getOpenFileNames()
        self.lineEdit.setText(path[0][0])
        if path[0][0][-4:] == '.txt' or path[0][0][-4:] == '.TXT':
            with open(path[0][0],'r') as f:
                text = f.read()
            self.plainTextEdit.setPlainText(text)
        else:
            self.plainTextEdit.setPlainText('需要.txt文件')

    def button_box_accepted(self):
        speaker = self.lineEdit_name.text()
        text = self.plainTextEdit.toPlainText()
        if speaker == '':
            if text == '':
                self.label.setText('设定文本（不能为空）')
            else:
                real_basic_UI.convers_text_from_import_UI = text


                self.Dialog.reject()
        else:
            if text == '':
                real_basic_UI.CALL_NAME = str(speaker)
                self.Dialog.reject()
            else:
                real_basic_UI.CALL_NAME = str(speaker)
                real_basic_UI.convers_text_from_import_UI = text
                self.Dialog.reject()


if __name__ == '__main__':
    if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        Widget = Ui_Dialog(Dialog)
        Widget.setupUi()
        Widget.retranslateUi()
        Widget.Dialog.show()
        app.exec()