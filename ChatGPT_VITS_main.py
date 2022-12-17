# 这是一个python文件
# 开发时间：2022/12/15 17:24
# 编写时请注意备注

import real_basic_UI
import use_main
import chatgpt_main

import sys
import import_UI
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = real_basic_UI.windows()
    Widget = real_basic_UI.Ui_Form()
    Widget.setupUi(Form)
    Form.show()
    app.exec()

