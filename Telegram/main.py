# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
import random
import threading
import os


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.list_driver = []
        self.so_acc = 0
        self.ten_acc = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 643)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 671, 701))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 801, 691))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.063, y1:0.0735455, x2:1, y2:1, stop:0 rgba(0, 72, 126, 255), stop:1 rgba(188, 204, 252, 255));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(60, 30, 201, 81))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 140, 201, 81))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 201, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 190, 201, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setGeometry(QtCore.QRect(290, 30, 201, 81))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(290, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.00568182, stop:0 rgba(108, 255, 131, 255), stop:0.568182 rgba(0, 255, 72, 255), stop:1 rgba(88, 209, 121, 255));\n"
"background-color: rgb(170, 85, 0);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 600, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Old English Text MT")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 380, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.063, y1:0.0735455, x2:1, y2:1, stop:0 rgba(255, 238, 3, 255), stop:1 rgba(216, 51, 252, 255));\n"
"border-radius: 5px;\n"
"color: rgb(170, 0, 0);\n"
"font: 12pt \"Bahnschrift\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 450, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.063, y1:0.0735455, x2:1, y2:1, stop:0 rgba(255, 238, 3, 255), stop:1 rgba(216, 51, 252, 255));\n"
"border-radius: 5px;\n"
"color: rgb(170, 0, 0);\n"
"font: 12pt \"Bahnschrift\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.00568182, stop:0 rgba(108, 255, 131, 255), stop:0.568182 rgba(0, 255, 72, 255), stop:1 rgba(88, 209, 121, 255));\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 520, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.063, y1:0.0735455, x2:1, y2:1, stop:0 rgba(255, 238, 3, 255), stop:1 rgba(216, 51, 252, 255));\n"
"border-radius: 5px;\n"
"color: rgb(170, 0, 0);\n"
"font: 12pt \"Bahnschrift\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.00568182, stop:0 rgba(108, 255, 131, 255), stop:0.568182 rgba(0, 255, 72, 255), stop:1 rgba(88, 209, 121, 255));\n"
"background-color: rgb(255, 85, 255);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        def khoitao():
                chrome_options = webdriver.ChromeOptions()
                prefs = {"profile.default_content_setting_values.notifications" : 2}
                chrome_options.add_experimental_option("prefs",prefs)
                #chrome_options.headless = True
                return webdriver.Chrome('./chromedriver.exe',chrome_options=chrome_options)





        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Bot Telegram"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Link group (t.me/xxx) cách nhau bởi dấu ;"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Nội dung chat đầu tiên cách nhau bởi dấu ;"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Thời gian chat cách nhau giữa các acc"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Thời gian chờ rồi sửa tin nhắn, profile"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Nội dung chat muốn chỉnh sửa"))
        def dung():
                os.system("taskkill /f /im chrome.exe")
                os.system("taskkill /f /im chromedriver.exe")
        def kill():
                x = threading.Thread(target=dung)
                x.start()
        self.pushButton.clicked.connect(kill)
        self.pushButton.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "Code:  0358259167"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Thông báo tiến trình"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Thông báo tiến trình"))
        def start__():
                list_gr = self.textEdit.toPlainText()
                try:
                        list_gr = list_gr.split(';')
                except:
                        pass
                try:
                        for url_link_gr in list_gr:
                                for driver in self.list_driver:
                                        driver.get(url_link_gr)
                                        time.sleep(5)
                                        url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/a').get_attribute('href')
                                        driver.get(url)
                                        time.sleep(5)
                                        if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').text == 'JOIN GROUP':
                                                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').click()
                                                time.sleep(5)
                                        try:
                                                driver.find_element_by_id('editable-message-text').send_keys(random.choice(self.textEdit_2.toPlainText().split(';')))
                                                time.sleep(1)
                                                driver.find_element_by_id('editable-message-text').send_keys(Keys.ENTER)

                                        except:
                                                pass
                except:
                        for driver in self.list_driver:
                                        driver.get(list_gr)
                                        time.sleep(5)
                                        url = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/a').get_attribute('href')
                                        driver.get(url)
                                        time.sleep(5)
                                        if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').text == 'JOIN GROUP':
                                                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/button[1]').click()
                                                time.sleep(5)
        def chay():
                x = threading.Thread(target=start__)
                x.start()
        self.pushButton_2.clicked.connect(chay)
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Thông báo tiến trình"))
        def login(driver):
                driver.set_window_position(0,0)
                driver.get('https://web.telegram.org/z/')
                time.sleep(20)
                try:
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/button').click()
                        time.sleep(5)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[4]').click()
                        time.sleep(5)
                        self.ten_acc = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[1]/h3').text
                        self.so_acc = self.so_acc + 1
                except:
                        return login(driver)
        def add__nick():
                driver = khoitao()
                login(driver)
                self.lineEdit_5.setText('Đăng nhập thành công: '+self.ten_acc)
                self.lineEdit_3.setText('Số lượng acc : '+str(self.so_acc))
                self.list_driver.append(driver)
        def add_nick():
                x = threading.Thread(target=add__nick)
                x.start()
        self.pushButton_3.clicked.connect(add_nick)
        self.pushButton_3.setText(_translate("MainWindow", "Add Nick"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
