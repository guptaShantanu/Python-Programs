# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bs4
import urllib.request as url


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 40, 301, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 251, 31))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 160, 181, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 270, 741, 91))
        self.label_3.setStyleSheet("\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 380, 81, 31))
        self.label_4.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 380, 101, 31))
        self.label_5.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 420, 81, 31))
        self.label_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 420, 601, 131))
        self.label_7.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 248, 251);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 71, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Movie Search Engine"))
        self.label_2.setText(_translate("MainWindow", "Enter The movie Name"))
        self.label_4.setText(_translate("MainWindow", "Rating"))
        self.label_6.setText(_translate("MainWindow", "Cast"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

        self.pushButton.clicked.connect(self.search)

    def search(self):
        try:
            path="https://www.imdb.com/find?ref_=nv_sr_fn&q="+self.lineEdit.text()+"&s=all"
            http=url.urlopen(path)

            first_page = bs4.BeautifulSoup(http, 'lxml')

            tag=first_page.find('td',class_="result_text")

            a_tag=tag.find_all('a')

            path2="https://m.imdb.com"+a_tag[0]['href']
            http2=url.urlopen(path2)
            second_page=bs4.BeautifulSoup(http2, 'lxml')

            data=second_page.find('p',class_="plot-description")

            self.label_3.setText(data.text)


        except BaseException as e:
            print(e)
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
