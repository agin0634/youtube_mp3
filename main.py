# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 229)
        MainWindow.setMinimumSize(QtCore.QSize(781, 229))
        MainWindow.setMaximumSize(QtCore.QSize(781, 229))
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(540, 140, 221, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("color: rgb(158, 158, 158);\n"
"background-color: rgb(57, 57, 57);")
        self.downloadButton.setObjectName("downloadButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(20, 90, 741, 41))
        self.urlEdit.setStyleSheet("background-color: rgb(18, 18, 18);\n"
"color: rgb(152, 152, 152);")
        self.urlEdit.setObjectName("urlEdit")
        self.downloadButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton_2.setGeometry(QtCore.QRect(310, 140, 221, 71))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.downloadButton_2.setFont(font)
        self.downloadButton_2.setStyleSheet("color: rgb(158, 158, 158);\n"
"background-color: rgb(57, 57, 57);")
        self.downloadButton_2.setObjectName("downloadButton_2")

        self.retranslateUi(MainWindow)
        self.downloadButton.clicked.connect(MainWindow.eventDownload)
        self.downloadButton_2.clicked.connect(MainWindow.eventDownloadmp4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.downloadButton.setText(_translate("MainWindow", "下載(.mp3)"))
        self.label.setText(_translate("MainWindow", "YOUTUBE 網址"))
        self.downloadButton_2.setText(_translate("MainWindow", "下載(.mp4)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
