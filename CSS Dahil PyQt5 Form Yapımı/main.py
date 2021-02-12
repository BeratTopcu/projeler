

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(286, 245)
        Form.setMinimumSize(QtCore.QSize(286, 245))
        Form.setMaximumSize(QtCore.QSize(286, 245))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("python_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(81, 81, 81);\n"
"background-color: rgb(72, 72, 72);")
        self.surname = QtWidgets.QLineEdit(Form)
        self.surname.setGeometry(QtCore.QRect(70, 80, 181, 21))
        self.surname.setStyleSheet("QLineEdit{\n"
"background-color: rgb(212, 212, 212);\n"
"\n"
"border: 0.7px solid  rgb(0,0, 0); ;\n"
"\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"")
        self.surname.setText("")
        self.surname.setObjectName("surname")

        #self.surname.setEchoMode(QtWidgets.QLineEdit.Password)


        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 41, 21))
        self.label_3.setStyleSheet("color: rgb(255, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.kiz = QtWidgets.QRadioButton(Form)
        self.kiz.setGeometry(QtCore.QRect(160, 130, 61, 20))
        self.kiz.setStyleSheet("color: rgb(255, 255, 255);")
        self.kiz.setObjectName("kiz")
        self.cikis = QtWidgets.QPushButton(Form)
        self.cikis.setGeometry(QtCore.QRect(28, 190, 101, 28))
        self.cikis.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"border-radius: 13px; \n"
"border-style: outset;\n"
" \n"
"\n"
"                      \n"
"\n"
"\n"
"\n"
"\n"
"    background-color: rgb(206, 19, 22);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"    \n"
"    background-color: rgb(171, 38, 40);\n"
"    \n"
"    color: rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    background-color: rgb(255, 0, 4);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cikis.setIcon(icon1)
        self.cikis.setObjectName("cikis")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(70, 30, 181, 21))
        self.name.setStyleSheet("QLineEdit{\n"
"background-color: rgb(212, 212, 212);\n"
"\n"
"border: 0.7px solid  rgb(0,0, 0); ;\n"
"\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"")
        self.name.setText("")
        self.name.setObjectName("name")
        self.erkek = QtWidgets.QRadioButton(Form)
        self.erkek.setGeometry(QtCore.QRect(60, 130, 71, 20))
        self.erkek.setStyleSheet("color: rgb(255, 255, 255);")
        self.erkek.setObjectName("erkek")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 21, 21))
        self.label_4.setStyleSheet("color: rgb(255, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.uye_ol = QtWidgets.QPushButton(Form)
        self.uye_ol.setGeometry(QtCore.QRect(160, 190, 101, 28))
        self.uye_ol.setStyleSheet("QPushButton{\n"
"\n"
"\n"
"border-radius: 13px; \n"
"border-style: outset;\n"
" \n"
"    background-color: rgb(12, 200, 21);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"\n"
"    \n"
"    background-color: rgb(12, 154, 21);\n"
"\n"
"    \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"    \n"
"    background-color: rgb(0, 235, 35);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("sign up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uye_ol.setIcon(icon2)
        self.uye_ol.setObjectName("uye_ol")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p>Ad:</p></body></html>"))
        self.label_3.setText(_translate("Form", "Soyad:"))
        self.kiz.setText(_translate("Form", "Kız"))
        self.cikis.setText(_translate("Form", "Çıkış"))
        self.erkek.setText(_translate("Form", "Erkek"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>Ad:</p></body></html>"))
        self.label_4.setText(_translate("Form", "Ad:"))
        self.uye_ol.setText(_translate("Form", "Üye Ol"))


        
        


        self.uye_ol.clicked.connect(lambda :self.click1(self.name.text().capitalize(),self.surname.text().capitalize(),self.erkek.isChecked(),self.kiz.isChecked()))

        self.cikis.clicked.connect(self.click2)
    def click1(self,name,surname,erkek,kiz):
            pass
    def click2(self):
            sys.exit()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

