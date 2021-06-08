# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admitcadet1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import mysql.connector as m
class Ui_admitcadettohosp(object):
    def admit_Cadet_button_click(self):
        mydb = m.connect(host='localhost', user='root', password='student', database='sskal')
        mycursor = mydb.cursor()
        query = 'create table if not exists admitcadet (schoolno integer primary key,reason varchar(900) not null, dateofadmit date ) '
        mycursor.execute(query)
        roll_no = int(self.lineEdit.text())
        reason = (self.TextEdit.toPlainText())
        time_admit = self.dateEdit.text()
        print(time_admit)
        alist = time_admit.split('/')
        print(alist)
        conv_time_admit = datetime.datetime(int(alist[2]),int(alist[0]),int(alist[1]))
        # print(conv_time_admit)
        #conv_time_admit = datetime.datetime.strftime(time_admit,"%d/%m/%Y").strftime("%Y-%m-%d")
        #print(datetime.date(time_admit))
        #print(conv_time_admit)
        print(reason)
        # print((self.lineEdit.text()))
        # print(self.TextEdit.toPlainText())
        query = "insert into admitcadet values('%d','%s','%s')" %(roll_no,reason,conv_time_admit)
        mycursor.execute(query)
        mydb.commit()
    def setupUi(self, admitcadettohosp):
        admitcadettohosp.setObjectName("admitcadettohosp")
        admitcadettohosp.resize(821, 571)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        admitcadettohosp.setFont(font)
        admitcadettohosp.setStyleSheet("background-color: rgb(247, 231, 255);")
        self.centralwidget = QtWidgets.QWidget(admitcadettohosp)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(660, 20, 71, 91))
        self.label_5.setStyleSheet("image: url(:/newPrefix/Sanjeevani.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 10, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 20, 121, 81))
        self.label_7.setStyleSheet("image: url(:/newPrefix/schoologo.jpg);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 180, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 180, 141, 31))
        self.lineEdit.setStyleSheet("font: 12pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 230, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 360, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.TextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(360, 230, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.TextEdit.setFont(font)
        self.TextEdit.setStyleSheet("font: 12pt \"Arial\";")
        self.TextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 450, 111, 61))
        self.pushButton.setStyleSheet("image: url(:/newPrefix/admitcadetbutton.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.admit_Cadet_button_click)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 450, 101, 61))
        self.pushButton_2.setStyleSheet("image: url(:/newPrefix/cancel - Copy.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(admitcadettohosp.hide)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 221, 331))
        self.label_9.setStyleSheet("image: url(:/newPrefix/admitcadetimage.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(360, 350, 221, 31))
        self.dateEdit.setStyleSheet("font: 10pt \"Arial\";")
        self.dateEdit.setObjectName("dateTimeEdit")
        admitcadettohosp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(admitcadettohosp)
        self.statusbar.setObjectName("statusbar")
        admitcadettohosp.setStatusBar(self.statusbar)

        self.retranslateUi(admitcadettohosp)
        QtCore.QMetaObject.connectSlotsByName(admitcadettohosp)

    def retranslateUi(self, admitcadettohosp):
        _translate = QtCore.QCoreApplication.translate
        admitcadettohosp.setWindowTitle(_translate("admitcadettohosp", "MainWindow"))
        self.label_3.setText(_translate("admitcadettohosp", "SAINIK SCHOOL KALIKIRI"))
        self.label_4.setText(_translate("admitcadettohosp", "SANJEEVANI"))
        self.label.setText(_translate("admitcadettohosp", "ROLL NO"))
        self.label_2.setText(_translate("admitcadettohosp", "REASON"))
        self.label_6.setText(_translate("admitcadettohosp", "DATE AND TIME"))

import Sanjeevani
import admitcadetbutton
import admitcadetimage
import cancel
import schoologo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admitcadettohosp = QtWidgets.QMainWindow()
    ui = Ui_admitcadettohosp()
    ui.setupUi(admitcadettohosp)
    admitcadettohosp.show()
    sys.exit(app.exec_())

