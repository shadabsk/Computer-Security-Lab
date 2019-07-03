# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bmi.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import os
import sys
import logging

LOG_FILE_Detailed_Info = "Detailed_Info.log"
LOG_FILE_Error = "Error.log"


def setup_logger(logger_name, log_file, level=logging.INFO):
    log_setup = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s:%(levelno)s:%(levelname)s:%(pathname)s:%(funcName)s:%(lineno)d:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    log_setup.setLevel(level)
    log_setup.addHandler(fileHandler)
    log_setup.addHandler(streamHandler)

def logger(msg, level, logfile):
    if logfile == 'Detailed_Info'   : log = logging.getLogger('Detailed_Info')
    if logfile == 'Error'   : log = logging.getLogger('Error') 
    if level == 'info'    : log.info(msg) 
    if level == 'warning' : log.warning(msg)
    if level == 'error'   : log.error(msg)

setup_logger('Detailed_Info', LOG_FILE_Detailed_Info)
setup_logger('Error', LOG_FILE_Error)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(320, 30, 161, 111))
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.quitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 5, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
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
        self.outputLabel.setText(_translate("MainWindow", "Output"))
        self.label_2.setText(_translate("MainWindow", "Weight"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.pushButton.clicked.connect(self.onClick)
        self.quitButton.clicked.connect(self.onQuit)

    def onClick(self):
        logger('Calculate Button clicked', 'info', 'Detailed_Info')
        if self.lineEdit.text() == '':
        	logger('height not specified', 'error', 'Error')
        	QtWidgets.QMessageBox.about(self, "BMI", "Type something in height field")
        	logger('OK Button Clicked', 'info', 'Detailed_Info') 
        if self.lineEdit_2.text() == '':
        	logger('mass not specified', 'error', 'Error')
        	QtWidgets.QMessageBox.about(self, "BMI", "Type something in mass field")
        	logger('OK Button Clicked', 'info', 'Detailed_Info')
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
            height = float(self.lineEdit.text())
            mass = float(self.lineEdit_2.text())

            bmi = mass / (height*height)
            bmi = round(bmi,2)
            logger('Height Given as {}'.format(height), 'info', 'Detailed_Info')
            logger('mass Given as {}'.format(mass), 'info', 'Detailed_Info')
            self.outputLabel.setText(str(bmi))
            logger('BMI Caclulated as {}'.format(bmi), 'info', 'Detailed_Info')

    def onQuit(self):
    	logger('Quit Button Clicked', 'info', 'Detailed_Info')
    	logger('Application Closed', 'info', 'Detailed_Info')
    	exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    logger('------------------------------------Application Launched------------------------------------', 'info', 'Detailed_Info')
    sys.exit(app.exec_())
