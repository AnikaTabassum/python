# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qus.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rb1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb1.setGeometry(QtCore.QRect(290, 360, 95, 20))
        self.rb1.setObjectName("rb1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 80, 331, 241))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.rb2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb2.setGeometry(QtCore.QRect(410, 360, 95, 20))
        self.rb2.setObjectName("rb2")
        self.rb3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb3.setGeometry(QtCore.QRect(410, 400, 95, 20))
        self.rb3.setObjectName("rb3")
        self.rb4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb4.setGeometry(QtCore.QRect(290, 400, 95, 20))
        self.rb4.setObjectName("rb4")
        self.object_label = QtWidgets.QLabel(self.centralwidget)
        self.object_label.setGeometry(QtCore.QRect(270, 20, 251, 41))
        self.object_label.setAlignment(QtCore.Qt.AlignCenter)
        self.object_label.setObjectName("object_label")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(290, 490, 201, 51))
        self.result.setAutoFillBackground(True)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.submitBut = QtWidgets.QPushButton(self.centralwidget)
        self.submitBut.setGeometry(QtCore.QRect(340, 440, 93, 28))
        self.submitBut.setObjectName("submitBut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setDB()
        self.submitBut.clicked.connect(self.getText)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rb1.setText(_translate("MainWindow", "Mango"))
        self.rb2.setText(_translate("MainWindow", "Banana"))
        self.rb3.setText(_translate("MainWindow", "Cherry"))
        self.rb4.setText(_translate("MainWindow", "Apple"))
        self.object_label.setText(_translate("MainWindow", "    What is the Object?"))
        self.submitBut.setText(_translate("MainWindow", "submit"))

    def setDB(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT imagePath FROM questions"
        myCursor.execute(sql)
        row=myCursor.fetchone()
        for file in row:
            print(file)
            ifileName=str(file)
            #print("lol"+ifileName)
            if ifileName:
                self.setImage(ifileName)
        

    def setImage(self, ifileName):
        #ifileName="img.jpg"
        pixmap=QtGui.QPixmap(ifileName)
        pixmap=pixmap.scaled(self.label.width(),
            self.label.height(), QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

    def checkAnswer(self,ans):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        myCursor = mydb.cursor(buffered=True)
        sql = "SELECT answer FROM questions"
        myCursor.execute(sql)
        row=myCursor.fetchone()
        for file in row:
            print(file)
            answer=str(file)
            if ans.lower()==answer.lower():
                print("matched")
                self.result.setText("correct answer!")
                newcur=mydb.cursor()
                sql = "UPDATE questions set result='correct' where qid=1"
                newcur.execute(sql)
                mydb.commit()
            else:
                print("not matched")
                self.result.setText("wrong answer!")
                newcur=mydb.cursor()
                sql = "UPDATE questions set result='incorrect' where qid=1"
                newcur.execute(sql)
                mydb.commit()
        myCursor.close()
        mydb.close()
        

    def getText(self):
        if self.rb1.isChecked():
            print(self.rb1.text())
            self.checkAnswer(self.rb1.text())
        if self.rb2.isChecked():
            print(self.rb2.text())
            self.checkAnswer(self.rb2.text())
        if self.rb3.isChecked():
            print(self.rb3.text())
            self.checkAnswer(self.rb3.text())
        if self.rb4.isChecked():
            print(self.rb4.text())
            self.checkAnswer(self.rb4.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

