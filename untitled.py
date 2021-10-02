# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication, QDialog
import thread
import os
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )

class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 896)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 531, 871))
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.063, y1:0.0735455, x2:1, y2:1, stop:0 rgba(0, 72, 126, 255), stop:1 rgba(188, 204, 252, 255));")
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(30, 180, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(0, 85, 255);\n"
"background-color: rgb(255, 255, 255,0);\n"
"background-color: rgb(0, 255, 127);")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 20, 82);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 201, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(240, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 5px;\n"
"color: rgb(0, 85, 127);\n"
"background-color: rgb(0, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 40, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 255, 127);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 50, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 20, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 350, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(0, 85, 255);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 20, 82);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 50, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 520, 451, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"background-color: rgb(0, 255, 127);\n"
"color: rgb(85, 85, 255);")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 20, 82);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setGeometry(QtCore.QRect(30, 40, 281, 81))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 150, 281, 131))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(350, 200, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(340, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setGeometry(QtCore.QRect(330, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border-radius: 5px;\n"
"color: rgb(170, 0, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(330, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(350, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,0);")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 820, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(170, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(360, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(370, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(255, 20, 82);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 516, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def thumuc(self):
        fname = QFileDialog.getOpenFileName(self,'Open file','C:\\Users')
        self.lineEdit.setText(fname[0])   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Telegram By Nguyễn Hoàng"))
        self.groupBox.setTitle(_translate("MainWindow", "Thay Đổi Avatar"))

        def thay_anh():
                file_name_nb = [self.lineEdit_3.text(),self.lineEdit.text()]
                thread.change__avatar(file_name_nb)
        def thay__anh():
                x = threading.Thread(target=thay_anh)
                x.start()
        self.pushButton_4.setText(_translate("MainWindow", "Run"))
        self.pushButton_4.clicked.connect(thay__anh)

        

        self.pushButton.clicked.connect(self.thumuc)
        self.pushButton.setText(_translate("MainWindow", "Browse"))

        self.groupBox_2.setTitle(_translate("MainWindow", "Đăng Nhập"))
        self.label.setText(_translate("MainWindow", "Số nick cần chạy"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Thay Đổi Tên"))
        def change__name():
                file_name_nb = [self.lineEdit_3.text(),self.lineEdit.text(),self.lineEdit_4.text()]
                thread.change__name(file_name_nb)
        def doiten():
                x = threading.Thread(target=change__name)
                x.start()
        self.pushButton_5.clicked.connect(doiten)
        self.pushButton_5.setText(_translate("MainWindow", "Run"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Tên muốn thay đổi"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Auto Chat"))

        def chat():
                file_name_nb = [self.lineEdit_3.text(),self.textEdit.toPlainText(),self.textEdit_2.toPlainText(),self.lineEdit_5.text()]
                thread.chat_ok(file_name_nb)
        def chat_1():
                x = threading.Thread(target=chat)
                x.start()
        self.pushButton_6.clicked.connect(chat_1)
        self.pushButton_6.setText(_translate("MainWindow", "Run"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Link nhóm cách nhau bởi dấu ;"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Nội dung chat cách nhau bằng dấu |"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "5,10s"))
        self.label_2.setText(_translate("MainWindow", "TIMER"))

        def jonn__gr1():
                file_name_nb = [self.lineEdit_3.text(),self.textEdit.toPlainText()]
                thread.join_gr(file_name_nb)
        def jonr1():
                x = threading.Thread(target=jonn__gr1)
                x.start()
        self.pushButton_7.clicked.connect(jonr1)
        self.pushButton_7.setText(_translate("MainWindow", "Join"))
        self.label_4.setText(_translate("MainWindow", "Tự động tham"))
        self.label_5.setText(_translate("MainWindow", "gia nhóm"))
        self.label_3.setText(_translate("MainWindow", "Hỗ Trợ Code: Hoàng 0358259167"))
        self.label_6.setText(_translate("MainWindow", "Auto Telegram"))
        def dung():
                os.system("taskkill /f /im chrome.exe")
                os.system("taskkill /f /im ._cache_chromedriver.exe")
        def kill():
                x = threading.Thread(target=dung)
                x.start()
        self.pushButton_8.clicked.connect(dung)
        self.pushButton_8.setText(_translate("MainWindow", "STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
