# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import traceback


class Ui_splash_frame(object):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sendit = False

    def setupUi(self, splash_frame):
        splash_frame.setObjectName("splash_frame")
        splash_frame.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(splash_frame)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 90, 451, 311))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 450, 241, 71))
        self.pushButton.setStyleSheet("font: 75 22pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 571))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 321, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 100, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 180, 321, 51))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 270, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 801, 561))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(250, 0, 20, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setGeometry(QtCore.QRect(260, 360, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 390, 421, 71))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.send_button = QtWidgets.QPushButton(self.frame_2)
        self.send_button.setGeometry(QtCore.QRect(700, 390, 75, 71))
        self.send_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(55, 255, 41);\n"
                                       "font: 75 16pt \"MS Shell Dlg 2\";\n"
                                       "selection-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.send_button.setObjectName("send_button")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 480, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(500, 480, 121, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.chat_list = QtWidgets.QListWidget(self.frame_2)
        self.chat_list.setGeometry(QtCore.QRect(270, 20, 511, 331))
        self.chat_list.setObjectName("chat_list")
        self.friend_list = QtWidgets.QListWidget(self.frame_2)
        self.friend_list.setGeometry(QtCore.QRect(30, 20, 201, 521))
        self.friend_list.setObjectName("friend_list")
        splash_frame.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(splash_frame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        splash_frame.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(splash_frame)
        self.statusbar.setObjectName("statusbar")
        splash_frame.setStatusBar(self.statusbar)

        self.retranslateUi(splash_frame)
        QtCore.QMetaObject.connectSlotsByName(splash_frame)

    def retranslateUi(self, splash_frame):
        _translate = QtCore.QCoreApplication.translate
        splash_frame.setWindowTitle(_translate("splash_frame", "MainWindow"))
        self.pushButton.setText(_translate("splash_frame", "GO --------->>"))
        self.pushButton_2.setText(_translate("splash_frame", "Submit"))
        self.pushButton_4.setText(_translate("splash_frame", "PushButton"))
        self.send_button.setText(_translate("splash_frame", "SEND"))
        self.pushButton_6.setText(_translate("splash_frame", "PushButton"))
        self.pushButton_7.setText(_translate("splash_frame", "PushButton"))
        self.frame.hide()

        self.pushButton.clicked.connect(self.show)
        self.send_button.clicked.connect(self.send)
        threading.Thread(target=self.start_server).start()
        self.pushButton_2.clicked.connect(self.reg)


    def reg(self):
        name=self.lineEdit.text()
        finall='::name::'+name
        self.soc.sendall(finall.encode("utf8"))
        self.soc.send
        self.frame.show()
        self.frame_2.show()

    def start_server(self):
        pass
        # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # host = "127.0.0.1"
        # port = 80
        #
        # try:
        #     self.soc.connect((host, port))
        # except:
        #     print("Connection error")
        #     sys.exit()

        # print("Enter 'quit' to exit")
        # username = input("Enter your name : ")
        # self.soc.sendall(username.encode("utf8"))
        # self.soc.send
        # message = input(" -> ")

        # while message != 'quit':
        #     self.soc.sendall(message.encode("utf8"))
        #     data = self.soc.recv(1024)
        #     print(data.decode())
        #
        #     message = input(" -> ")
        #
        # self.soc.send(b'--quit--')
    def recv(self):
        while True:

            data = self.soc.recv(1024)
            print(data.decode())
            item = QtWidgets.QListWidgetItem()
            self.chat_list.addItem(item)
            item.setText(data.decode())
            item.setTextAlignment(QtCore.Qt.AlignLeft)


    def send(self):
        msg = self.lineEdit_4.text()
        self.soc.sendall(msg.encode("utf8"))
        self.soc.send
        item = QtWidgets.QListWidgetItem()
        self.chat_list.addItem(item)
        item.setText(msg)
        item.setTextAlignment(QtCore.Qt.AlignRight)


    # def client_thread(self, connection, ip, port, max_buffer_size=5120):
    #     is_active = True
    #
    #     while is_active:
    #         client_input = self.receive_input(connection, max_buffer_size)
    #
    #         if "--QUIT--" in client_input:
    #             print("Client is requesting to quit")
    #             connection.close()
    #             print("Connection " + ip + ":" + port + " closed")
    #             is_active = False
    #         else:
    #             print("Processed result: {}".format(client_input))
    #             # return ip,client_input
    #             # print("Processed result: {}".format(client_input))
    #             item = QtWidgets.QListWidgetItem()
    #             self.chat_list.addItem(item)
    #             item.setText(client_input)
    #             item.setTextAlignment(QtCore.Qt.AlignRight)
    #
    #             print(client_input)
    #             # msg = input("-> ")
    #             # connection.sendall(msg.encode("utf8"))
    #             if self.sendit:
    #                 msg = self.lineEdit_4.text()
    #                 connection.sendall(msg.encode("utf8"))
    #                 sendit = False

    # def receive_input(self, connection, max_buffer_size):
    #     while True:
    #
    #         client_input = connection.recv(max_buffer_size)
    #         client_input_size = sys.getsizeof(client_input)
    #
    #         if client_input_size > max_buffer_size:
    #             print("The input size is greater than expected {}".format(client_input_size))
    #
    #         decoded_input = client_input.decode("utf8").rstrip()  # decode and strip end of line
    #         return decoded_input

    def show(self):
        host = "127.0.0.1"
        port = 80

        try:
            self.soc.connect((host, port))
            print("jai ho")
            threading.Thread(target=self.recv).start()
        except:
            print("Connection error")
            sys.exit()
        self.frame.show()
        self.frame_2.hide()

    def sendmsg(self, data):
        self.soc.sendall(self.lineEdit_4.text().encode("utf8"))
        self.soc.send
        item = QtWidgets.QListWidgetItem()
        self.chat_list.addItem(item)
        item.setText(self.lineEdit_4.text())
        item.setTextAlignment(QtCore.Qt.AlignRight)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    splash_frame = QtWidgets.QMainWindow()
    ui = Ui_splash_frame()
    ui.setupUi(splash_frame)
    splash_frame.show()
    sys.exit(app.exec_())
