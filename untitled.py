# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 726)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 121, 71))
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(23, 255, 81);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 20, 801, 651))
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(50, 30, 431, 161))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 230, 141, 81))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(23, 255, 81);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 0);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 230, 151, 81))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(23, 255, 81);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 255, 255);\n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 230, 141, 81))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(23, 255, 81);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 0);\n"
"\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(220, 340, 151, 81))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"border-radius:10px;\n"
"font: 87 8pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(23, 255, 81);\n"
"    border: 0px solid\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 0);\n"
"\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(30, 5, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(320, 20, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(340, 70, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(350, 160, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setGeometry(QtCore.QRect(190, 0, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(280, 130, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 142, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        self.label_6.setGeometry(QtCore.QRect(360, 240, 261, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(360, 180, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(250, 0, 361, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_4)
        self.label_8.setGeometry(QtCore.QRect(260, 161, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 168, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(348, 210, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color:rgb(82,84,99);\n"
"border:none;\n"
"border-radius:20px;}\n"
"\n"
"QPushButton::hover{background-color:black;}\n"
"QPushButton::focus{background-color:green;}\n"
"\n"
" ")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(360, 310, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_10 = QtWidgets.QLabel(self.page_5)
        self.label_10.setGeometry(QtCore.QRect(160, 110, 471, 291))
        self.label_10.setStyleSheet("background-color:rgba(66,64,66,0.7);border-radius:20px\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.giris_kullanici_line = QtWidgets.QLineEdit(self.page_5)
        self.giris_kullanici_line.setGeometry(QtCore.QRect(350, 270, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.giris_kullanici_line.setFont(font)
        self.giris_kullanici_line.setStyleSheet("background-color:rgb(29,37,97);\n"
"border:none;\n"
"border-radius:15px;\n"
"color:white;\n"
"padding-left:20px;\n"
"padding-right:20px\n"
"")
        self.giris_kullanici_line.setObjectName("giris_kullanici_line")
        self.giris_kullanici_line_2 = QtWidgets.QLineEdit(self.page_5)
        self.giris_kullanici_line_2.setGeometry(QtCore.QRect(350, 200, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.giris_kullanici_line_2.setFont(font)
        self.giris_kullanici_line_2.setStyleSheet("background-color:rgb(29,37,97);\n"
"border:none;\n"
"border-radius:15px;\n"
"color:white;\n"
"padding-left:20px;\n"
"padding-right:20px\n"
"")
        self.giris_kullanici_line_2.setObjectName("giris_kullanici_line_2")
        self.label_11 = QtWidgets.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(200, 275, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_5)
        self.label_12.setGeometry(QtCore.QRect(200, 204, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.page_5)
        self.label_13.setGeometry(QtCore.QRect(300, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 340, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{color: rgb(255, 255, 255);\n"
"background-color:rgb(82,84,99);\n"
"border:none;\n"
"border-radius:20px;}\n"
"\n"
"QPushButton::hover{background-color:black;}\n"
"QPushButton::focus{background-color:green;}\n"
"\n"
" ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ana Sayfa"))
        self.label.setText(_translate("MainWindow", "Hoş Geldiniz..\n"
"Bu uygulama Derste verilen örneklerin arayüz çalışmasıdır"))
        self.pushButton_2.setText(_translate("MainWindow", "Hafta\n"
"Gün Çalışması"))
        self.pushButton_3.setText(_translate("MainWindow", "Kare ve Küp Çalışması"))
        self.pushButton_5.setText(_translate("MainWindow", "4 Sayı ile \n"
"Tek ve Çift Çalışması"))
        self.pushButton_7.setText(_translate("MainWindow", "Kullanıcı ve Şifre\n"
"Çalışması"))
        self.label_2.setText(_translate("MainWindow", "Haftanın gün sayısını yazınız\n"
"(1-7)"))
        self.pushButton_8.setText(_translate("MainWindow", "Tıkla"))
        self.label_4.setText(_translate("MainWindow", "100\'den büyükse karesini\n"
"küçükse küpünü alan program"))
        self.label_5.setText(_translate("MainWindow", "Sayı:"))
        self.pushButton_9.setText(_translate("MainWindow", "Tıkla"))
        self.label_7.setText(_translate("MainWindow", " Çift ise 4 ile çarpılacak\n"
" tek ise 9 ile toplanacak "))
        self.label_8.setText(_translate("MainWindow", "Sayı: "))
        self.pushButton_10.setText(_translate("MainWindow", "Tıkla"))
        self.label_9.setText(_translate("MainWindow", "asdasd"))
        self.label_11.setText(_translate("MainWindow", "Şifre:"))
        self.label_12.setText(_translate("MainWindow", "Kullanıcı adı:"))
        self.label_13.setText(_translate("MainWindow", "LOGİN THE SYSTEM"))
        self.pushButton_4.setText(_translate("MainWindow", "Giriş"))