from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
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

#logging.basicConfig(filename='test.log', level=logging.INFO,
 #                   format='%(asctime)s:%(levelname)s:%(message)s')
 
class Example(QtWidgets.QMainWindow):
    def __init__(self):
        logger('------------------------------------Application Launched------------------------------------', 'info', 'Detailed_Info')
        super(Example, self).__init__()
        uic.loadUi('bmi.ui', self)
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


            


app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
