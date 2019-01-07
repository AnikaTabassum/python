# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\python\test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imglabel1 = QtWidgets.QLabel(self.centralwidget)
        self.imglabel1.setGeometry(QtCore.QRect(50, 30, 241, 241))
        self.imglabel1.setMouseTracking(True)
        self.imglabel1.setAutoFillBackground(True)
        self.imglabel1.setFrameShape(QtWidgets.QFrame.Panel)
        self.imglabel1.setLineWidth(3)
        self.imglabel1.setText("")
        self.imglabel1.setObjectName("imglabel1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.viewImage()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def setImage(self, ifileName):
        pixmap=QtGui.QPixmap(ifileName)
        pixmap=pixmap.scaled(self.imglabel1.width(),
            self.imglabel1.height(), QtCore.Qt.KeepAspectRatio)
        self.imglabel1.setPixmap(pixmap)
        self.imglabel1.setAlignment(QtCore.Qt.AlignCenter)

    def viewImage(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT imageName FROM item"
        myCursor.execute(sql)
        row=myCursor.fetchone()
        for file in row:
            print(file)
            ifileName=str(file)
            #print("lol"+ifileName)
            if ifileName:
                self.setImage(ifileName)
        myCursor.close()
        mydb.close()
        
        #row=myCursor.fetchone()
         
        ##=====================================
        #ei string theke amake bracket ar comma alada kore dao frans :3
        #ifileName="C:/Users/dell/Desktop/test.jpg"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

