from PyQt5.QtWidgets import QApplication
import sys
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from untitled import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QMessageBox,QCalendarWidget



class Calisma(QMainWindow):
    def __init__(self):
        super(Calisma, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ana_ekran = 0
        self.hafta_gun = 1
        self.kare_kup = 2
        self.cift_tek = 3
        self.kullanici_sifre = 4
        self.kayit_ol = 5

        self.ui.pushButton_8.clicked.connect(self.hafta_calismasi_iki)
        self.ui.pushButton_9.clicked.connect(self.kare_kup_iki)
        self.ui.pushButton_10.clicked.connect(self.cift_tek_calismasi_iki)
        self.ui.pushButton_4.clicked.connect(self.kullanici_sifre_calismasi_iki)

        self.ui.pushButton.clicked.connect(self.ana_sayfa)
        self.ui.pushButton_2.clicked.connect(self.hafta_calismasi)
        self.ui.pushButton_3.clicked.connect(self.kare_kup_calismasi)
        self.ui.pushButton_5.clicked.connect(self.cift_tek_calismasi)
        self.ui.pushButton_7.clicked.connect(self.kullanici_sifre_calismasi)



    def ana_sayfa(self):
        self.ui.stackedWidget.setCurrentIndex(self.ana_ekran)




    def kayit_ol_1(self):
        self.ui.stackedWidget.setCurrentIndex(self.kayit_ol)


    def kullanici_sifre_calismasi_iki(self):
        kadi = "mehmetnuri"
        ksifre = "123456"
        email = "info@mehmetnuri.net"

        kadi_1 = self.ui.giris_kullanici_line_2.text()
        ksifre_1 = self.ui.giris_kullanici_line.text()

        if (kadi_1 == kadi or email == kadi_1) and (ksifre_1 == ksifre):
            self.ui.statusbar.showMessage("GİRİŞ BAŞARILI",2000)
            self.ui.statusbar.setStyleSheet("background-color : white")
        else:
            messagebox = QMessageBox()
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setWindowTitle("Hatalı Giriş")
            messagebox.setText("Kullanıcı adı veya Şifre Hatalı")
            messagebox.setStandardButtons(QMessageBox.Ok)
            buton_ok = messagebox.button(QMessageBox.Ok)
            buton_ok.setText("Tamam")
            messagebox.exec_()


    def kullanici_sifre_calismasi(self):
        self.ui.stackedWidget.setCurrentIndex(self.kullanici_sifre)


    def cift_tek_calismasi_iki(self):
        cift_tek_line = int((self.ui.lineEdit_3.text()))


        if cift_tek_line%2==0:
            sonuc = cift_tek_line*4
            self.ui.label_9.setText(str(sonuc))
        elif cift_tek_line%2!=0:
            sonuc_1 = cift_tek_line+9
            self.ui.label_9.setText(str(sonuc_1))
        else:
            self.ui.label_9.setText("Düzgün değer gir")






    def cift_tek_calismasi(self):
        self.ui.stackedWidget.setCurrentIndex(self.cift_tek)

    def kare_kup_iki(self):
        kare_kup_line = int(self.ui.lineEdit_2.text())


        if kare_kup_line>100:
            kare_al = kare_kup_line**2
            self.ui.label_6.setText(str(kare_al))
        elif kare_kup_line<100:
            kup_al = kare_kup_line**3
            self.ui.label_6.setText(str(kup_al))



    def kare_kup_calismasi(self):
        self.ui.stackedWidget.setCurrentIndex(self.kare_kup)


    def hafta_calismasi(self):
        self.ui.stackedWidget.setCurrentIndex(self.hafta_gun)


    def hafta_calismasi_iki(self):
        hafta_line = self.ui.lineEdit.text()

        if hafta_line == "1":
            self.ui.label_3.setText("Pazartesi")
        elif hafta_line == "2":
            self.ui.label_3.setText("Salı")
        elif hafta_line == "3":
            self.ui.label_3.setText("Çarşamba")
        elif hafta_line == "4":
            self.ui.label_3.setText("Perşembe")
        elif hafta_line == "5":
            self.ui.label_3.setText("Cuma")
        elif hafta_line == "6" or hafta_line == "7":
            self.ui.label_3.setText("Hafta Sonu")
        else:
            self.ui.label_3.setText("Lütfen belirtilen değerleri giriniz")




app=QApplication([])

kullanicilar=Calisma()
kullanicilar.show()


app.exec_()
