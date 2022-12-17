# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choosebg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import real_basic_UI

class Ui_Choosebg(object):
    def __init__(self,Choosebg):
        self.Choosebg = Choosebg
        self.path = ''

    def setupUi(self):
        self.Choosebg.setObjectName("Choosebg")
        self.Choosebg.resize(425, 127)
        self.Choosebg.setFixedSize(425, 127)
        self.Choosebg.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.Choosebg)
        self.buttonBox.setGeometry(QtCore.QRect(60, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(self.Choosebg)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.Choosebg)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 311, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.Choosebg)
        self.pushButton.setGeometry(QtCore.QRect(340, 20, 41, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked_push_button_choosebg)

        self.retranslateUi()
        self.buttonBox.accepted.connect(self.choosebg_accept)
        self.buttonBox.rejected.connect(self.Choosebg.reject)
        QtCore.QMetaObject.connectSlotsByName(self.Choosebg)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.Choosebg.setWindowTitle(_translate("Choosebg", "选择图片"))
        self.label.setText(_translate("Choosebg", "请选择JPG文件"))
        self.pushButton.setText(_translate("Choosebg", "..."))

    def clicked_push_button_choosebg(self):
        path = QtWidgets.QFileDialog.getOpenFileNames()
        if path[0][0][-4:] == '.JPG' or path[0][0][-4:] == '.jpg' or path[0][0][-4:] == '.PNG' or path[0][0][-4:] == '.png':
            self.lineEdit.setText(path[0][0])
            self.path = self.lineEdit.text()
        else:
            self.label.setText('需要.jpg或.png文件')

    def choosebg_accept(self):
        '''
        不能使用下面这个代码，否则循环调用了Widget
        real_basic_UI.Widget.label_2.setPixmap(QtGui.QPixmap(real_basic_UI.Backgroud_jpg_path))
        '''
        if self.path == '':
            self.label.setText('需要.jpg或.png文件,请选择路径')
        else:
            real_basic_UI.Backgroud_jpg_path = self.path
            self.Choosebg.reject()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    choosebg = QtWidgets.QDialog()
    choosebg_widget = Ui_Choosebg(choosebg)
    choosebg_widget.setupUi()
    choosebg_widget.Choosebg.show()
    app.exec()