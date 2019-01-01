# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\backend\additem.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(877, 709)
        Form.setMouseTracking(True)
        Form.setAutoFillBackground(True)
        self.imgLabel = QtWidgets.QLabel(Form)
        self.imgLabel.setGeometry(QtCore.QRect(310, 190, 241, 211))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setLineWidth(3)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.VideoLabel = QtWidgets.QLabel(Form)
        self.VideoLabel.setGeometry(QtCore.QRect(30, 200, 231, 171))
        self.VideoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.VideoLabel.setLineWidth(2)
        self.VideoLabel.setText("")
        self.VideoLabel.setObjectName("VideoLabel")
        self.audioLabel = QtWidgets.QLabel(Form)
        self.audioLabel.setGeometry(QtCore.QRect(590, 200, 221, 191))
        self.audioLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.audioLabel.setLineWidth(2)
        self.audioLabel.setText("")
        self.audioLabel.setObjectName("audioLabel")
        self.vidpushButton = QtWidgets.QPushButton(Form)
        self.vidpushButton.setGeometry(QtCore.QRect(130, 480, 93, 28))
        self.vidpushButton.setObjectName("vidpushButton")
        self.imgpushButton = QtWidgets.QPushButton(Form)
        self.imgpushButton.setGeometry(QtCore.QRect(380, 500, 93, 28))
        self.imgpushButton.setObjectName("imgpushButton")
        self.audpushButton = QtWidgets.QPushButton(Form)
        self.audpushButton.setGeometry(QtCore.QRect(630, 500, 93, 28))
        self.audpushButton.setObjectName("audpushButton")
        self.objpushButton = QtWidgets.QPushButton(Form)
        self.objpushButton.setGeometry(QtCore.QRect(290, 570, 311, 61))
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
        self.imglineEdit.setGeometry(QtCore.QRect(320, 430, 231, 51))
        self.imglineEdit.setObjectName("imglineEdit")
        self.auddlineEdit = QtWidgets.QLineEdit(Form)
        self.auddlineEdit.setGeometry(QtCore.QRect(590, 420, 191, 51))
        self.auddlineEdit.setObjectName("auddlineEdit")
        self.viddlineEdit_2 = QtWidgets.QLineEdit(Form)
        self.viddlineEdit_2.setGeometry(QtCore.QRect(30, 400, 231, 51))
        self.viddlineEdit_2.setObjectName("viddlineEdit_2")

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
        ifileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        print(ifileName)
        self.imglineEdit.setText(ifileName)
        if ifileName:
            pixmap=QtGui.QPixmap(ifileName)
            pixmap=pixmap.scaled(self.imgLabel.width(),
                self.imgLabel.height(), QtCore.Qt.KeepAspectRatio)
            self.imgLabel.setPixmap(pixmap)
            self.imgLabel.setAlignment(QtCore.Qt.AlignCenter)

    def setVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Video", "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads", "*.mp4")
        print(fileName)
        self.VideoLabel.setText(fileName)
        self.viddlineEdit_2.setText(fileName)


    def setAudio(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Audio", "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads", "*.mp3")
        print(fileName)
        self.audioLabel.setText(fileName)
        self.auddlineEdit.setText(fileName)

    def deleting(self):
        self.imgLabel.clear()
        self.imglineEdit.setText("")
        self.VideoLabel.clear()
        self.viddlineEdit_2.setText("")
        self.audioLabel.clear()
        self.auddlineEdit.setText("")
        self.addName.setText("")

    def additem(self):
        mydb = mysql.connector.connect(
                host = 'localhost',
                user = "anika",
                passwd = "hridita123",
                database = "loginDB"
                #auth_plugin='mysql_native_password'
                )
        ifileName=self.imglineEdit.text();
        vfileName=self.viddlineEdit_2.text();
        audfileName=self.auddlineEdit.text();
        print("printing"+ifileName)
        name=self.addName.text()
        myCursor = mydb.cursor()
        #sql="""LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SI_20180317_171204.jpg' INTO TABLE items"
        sql = "INSERT INTO itemss(name, imageName, videoName, audioName) \
        VALUES(%s, LOAD_FILE(%s), LOAD_FILE(%s), LOAD_FILE(%s))"
        val = (name, ifileName, vfileName, audfileName) 
       # val = (name, ifileName, vfileName, audfileName) 
        
        myCursor.execute(sql,val)
        mydb.commit()
        myCursor.close()
        mydb.close()

        messageBox = QtWidgets.QMessageBox()
        messageBox.setIcon(QtWidgets.QMessageBox.Information)
        messageBox.setWindowTitle("Item")
        messageBox.setText("Item added!")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close)
        messageBox.exec_()
        self.deleting()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

