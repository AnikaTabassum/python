# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\backend\additem2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(852, 609)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(90, 320, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")
        self.imgpushButton = QtWidgets.QPushButton(Form)
        self.imgpushButton.setGeometry(QtCore.QRect(380, 430, 93, 28))
        self.imgpushButton.setObjectName("imgpushButton")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(640, 320, 93, 28))
        self.audpushButton.setObjectName("audpushButton")
        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(270, 480, 311, 61))
        self.objpushButton.setObjectName("objpushButton")
        self.addName = QtWidgets.QLineEdit(Form)
        self.addName.setGeometry(QtCore.QRect(250, 50, 361, 101))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        self.addName.setFont(font)
        self.addName.setLocale(QtCore.QLocale(QtCore.QLocale.Bengali, QtCore.QLocale.Bangladesh))
        self.addName.setAlignment(QtCore.Qt.AlignCenter)
        self.addName.setObjectName("addName")
        self.imglineEdit = QtWidgets.QLineEdit(Form)
        self.imglineEdit.setGeometry(QtCore.QRect(290, 190, 261, 211))
        self.imglineEdit.setObjectName("imglineEdit")
        self.audlineEdit = QtWidgets.QLineEdit(Form)
        self.audlineEdit.setGeometry(QtCore.QRect(600, 190, 181, 91))
        self.audlineEdit.setObjectName("audlineEdit")
        self.vidlineEdit = QtWidgets.QLineEdit(Form)
        self.vidlineEdit.setGeometry(QtCore.QRect(50, 190, 181, 81))
        self.vidlineEdit.setObjectName("vidlineEdit")

        self.imgpushButton.clicked.connect(self.setImage)
        self.vidpushButton.clicked.connect(self.setVideo)
        self.audpushButton.clicked.connect(self.setAudio)
        self.objpushButton.clicked.connect(self.additem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.vidpushButton.setText(_translate("Form", "Add Video"))
        self.imgpushButton.setText(_translate("Form", "Add Image"))
        self.audpushButton.setText(_translate("Form", "Add audio"))
        self.objpushButton.setText(_translate("Form", "Add Object"))

    def setImage(self):
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit.setText(ifileName)


    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "", "*.mp4")
        print(fileName)
        self.vidlineEdit.setText(fileName)

    def setAudio(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Audio", "", "*.mp3")
        print(fileName)
        self.audlineEdit.setText(fileName)

    def additem(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        ifileName=self.imglineEdit.text();
        vfileName=self.vidlineEdit.text();
        audfileName=self.audlineEdit.text();
        name=self.addName.text()
        myCursor = mydb.cursor()
        sql = "INSERT INTO item(name, imageName, videoName, audioName) \
        VALUES(%s, %s, %s, %s)"
        val = (name, ifileName, vfileName, audfileName) 
        print(name)
        print(audfileName)
        myCursor.execute(sql, val)
        mydb.commit()
        myCursor.close()
        mydb.close()

        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Item")
        messageBox.setText("Item added!")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

