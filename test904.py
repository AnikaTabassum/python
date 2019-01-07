# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def dbClose:

    def prev_event(self,cid):

    def nxt_event(self,cid):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(130, 60, 361, 241))
        self.img.setMouseTracking(True)
        self.img.setAutoFillBackground(True)
        self.img.setFrameShape(QtWidgets.QFrame.Panel)
        self.img.setLineWidth(3)
        self.img.setText("")
        self.img.setObjectName("img")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(170, 340, 93, 28))

        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT object_id FROM item"
        myCursor.execute(sql)
        row=myCursor.fetchone()
        for file in row:
            cid
        self.prev.setObjectName("prev")
        self.prev.clicked.connect(self.prev_event(cid))


        self.nxt = QtWidgets.QPushButton(self.centralwidget)
        self.nxt.setGeometry(QtCore.QRect(380, 340, 93, 28))
        self.nxt.setObjectName("nxt")
        self.nxt.clicked.connect(self.nxt_event(cid))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 26))
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
        self.prev.setText(_translate("MainWindow", "Previous"))
        self.nxt.setText(_translate("MainWindow", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

